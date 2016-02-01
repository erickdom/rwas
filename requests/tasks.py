import re

import time

import datetime

import ast

import suds
from celery.app.task import Task
from subprocess import check_output, CalledProcessError

from celery.task import task
from suds.client import Client

from requests.models import Last_Whatsapp_Id, Request


class ReceiverTask(Task):
    queue_messages = []

    def encendervbox(self):
        print "Encendiendo Vbox"

    def check_valid_text(self, message):
        if re.match("^(\d{10,30})(\*)(\d+(\.\d{1,2})?)(\*)(\d{1,2})$", message):
            return 1

        elif re.match("^saldo$", message.lower()):
            return 2

        elif re.match("marco", message.lower()):
            return 3

        else:
            print "no se arma"
            return False

    def run(self):
        variable = "muchoooos"
        # for i in variable:
        #     print i
        #     time.sleep(1)
        # rows = []
        try:
            error = False
            last__id = Last_Whatsapp_Id.objects.last()
            try:
                output = check_output(
                        "adb shell 'sqlite3 /data/data/com.whatsapp/databases/msgstore.db \"select * from messages WHERE _id>{} AND key_from_me != 1;\"'".format(
                                last__id.whatsapp_id), shell=True)
                rows = output.split("|\r\n")
                del rows[-1]
            except CalledProcessError as e:
                error = True

            if error:
                self.encendervbox()
            else:
                for row in rows:
                    elements = row.split("|")
                    request_type = self.check_valid_text(elements[6])
                    if request_type:
                        date = datetime.datetime.fromtimestamp(int(elements[7]) / 1000).strftime("%Y-%m-%d %H:%M:%S")
                        print date
                        date_received = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                        request_message = Request.objects.create(
                                message=elements[6],
                                number=elements[1],
                                date_request=date,
                                request_type=request_type,
                                date_received=date_received
                        )
                        request_message.save()
                    last__id.whatsapp_id = elements[0]
                last__id.save()
                print self.queue_messages
            time.sleep(5)
        except Exception, e:
            print "Error " + str(e)


class SenderTask(Task):


    timeout = 5
    loop_time = 170

    def run(self, *args, **kwargs):

        requests = Request.objects.filter(response__exact=None)
        for request in requests:
            request.code = "00"
            request.response = "01"
            date_sent = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            request.date_sent = date_sent
            request.save()
            l1 = int(round(time.time() * 1000))
            l2 = int(l1 / 1000)
            k = "-1150867590"

            response =  self.tae_request(request.message, "8990000123", request.number, "http://www.ventamovil.com.mx:9110")
            print response
            responseeString =  response.get("msgResponse",None)

            str1 = """
            adb shell "sqlite3 /data/data/com.whatsapp/databases/msgstore.db \\"INSERT INTO messages (key_remote_jid, key_from_me, key_id, status, needs_push, data, timestamp, MEDIA_URL, media_mime_type, media_wa_type, MEDIA_SIZE, media_name , latitude, longitude, thumb_image, remote_resource, received_timestamp, send_timestamp, receipt_server_timestamp, receipt_device_timestamp, raw_data, media_hash, recipient_count, media_duration, origin) VALUES ('{}', 1,'{}-{}', 0,0, '{}',{},'','', 0, 0,'', 0.0,0.0,'','',{}, -1, -1, -1,0 ,'',0,0,0);\\""
            """.format(request.number, l2, k, responseeString, l1, l1)

            str2 = """ adb shell "sqlite3 /data/data/com.whatsapp/databases/msgstore.db \\"insert into chat_list (key_remote_jid) select '{}' where not exists (select 1 from chat_list where key_remote_jid='{}');\\"" """.format(
                    request.number, request.number)
            #
            str3 = """ adb shell "sqlite3 /data/data/com.whatsapp/databases/msgstore.db \\"update chat_list set message_table_id = (select max(messages._id) from messages) where chat_list.key_remote_jid='{}';\\"" """.format(
                    request.number)


            try:
                print check_output("adb shell pkill com.whatsapp", shell=True)
                print check_output("adb shell chmod 777 /data/data/com.whatsapp/databases/msgstore.db", shell=True)
                print check_output(str1, shell=True)
                print check_output(str2, shell=True)
                print check_output(str3, shell=True)
            except CalledProcessError as e:
                print e


    def tae_request(self, message, folio_android, sender, webservice):
        try:
            sender = sender[:13]
            sender = sender[-10:]

            folio = folio_android

            jsontosend = "{0}*{1}*{2}*{3}".format( message, folio, "99", sender )
            wsResp = self.buildWS(request_type=2, jsontosend=jsontosend)

            jsonResp = ast.literal_eval(wsResp)
            if jsonResp['Confirmation'] != "00":
                jsonResp = self.check_transaction(message, folio, sender, webservice)
                jsonResp['msgResponse'] = jsonResp.get('MSG_Response', None)
                jsonResp['Confirmation'] = jsonResp.get('Response', None)

                if not jsonResp['msgResponse']:
                    jsonResp['msgResponse'] = jsonResp.get('Description', None)

                if not jsonResp['Confirmation']:
                    jsonResp['Confirmation'] = jsonResp.get('Confirmation', None)

            return jsonResp

        except Exception, e:
            resp = {}
            resp['Description'] = "El proveedor TAE no responde"
            resp['Confirmation'] = "24"
            resp['FolioPos'] = folio
            resp['msgResponse'] = "Error al registrar una recarga {0}".format(e.message)
            return resp


    def buildWS(self, request_type, jsontosend):
        wsResp = "{}"
        try:
            client = Client("http://ventamovil.com.mx:9213/service.asmx?wsdl", timeout=self.loop_time)
        except Exception:
            raise Exception("No se pudo conectar con el Servicio de TAE")
        if request_type == 2:
            wsResp = client.service.sms_resume(jsontosend)
        elif request_type == 1:
            wsResp = client.service.sms_request_transaction(jsontosend)

        return wsResp

    def check_transaction(self, message, folio, sender, tae_url):

        check_transaction_dic = {}
        check_transaction_dic['Folio_Pos'] = str(folio)
        check_transaction_dic['User'] = str(sender)
        jsontosend = str(check_transaction_dic)
        resp = {}

        for cont_seg in range(self.loop_time):
            time.sleep(0.4)

            try:
                client = Client(tae_url, timeout=self.timeout)
            except suds.WebFault as details:
                continue

            try:
                ws_resp = client.service.sms_check_transaction(jsontosend)

                resp = ast.literal_eval(ws_resp)
                code_confirm = resp.get('Response', None)
                if code_confirm is None:
                    code_confirm = resp.get('Confirmation', None)

                if code_confirm and code_confirm != "24":
                    return resp

                if code_confirm == "17" and cont_seg >= 10:
                    resp['Description'] = "El proveedor TAE no responde"

            except Exception, e:
                pass

        # Fallback, no hubo respuesta
        resp['Description'] = "El proveedor TAE no responde"
        resp['msgResponse'] = "El proveedor TAE no responde"
        resp['Confirmation'] = "24"
        resp['FolioPos'] = folio
        return resp