from plataform import var_data_process
from plataform .wss.send_message_wss import MessageWSS
from plataform.controllers_proccess_data.process_data_operations import ProcessDataOperations
from plataform.controllers_proccess_data.process_analytics_data_alert import ProcessData_Alert

from logs_api.logs_api import logging_api

class AnalyzeData:
    def analizy_data_operation(message):
        try:
            if var_data_process.TYPE_OPERATION == "pre-analysis":
                data = ProcessData_Alert(message).process_data_version_1_alert(type_operation="pre-analysis")
                if data["direction"] != "---":
                    ProcessDataOperations.alert_operations(
                        obj_alert=data,
                        status_alert="pre-analysis",
                        )
                    logging_api(
                        process_log="info", log=f"status_alert: pre-analysis | data: {data}")

            elif var_data_process.TYPE_OPERATION == "activate-operation":
                data = ProcessData_Alert(message).process_data_version_1_alert(type_operation="activate-operation")
                if data["direction"] != "---":
                    MessageWSS.send_message_open_operation_alert(
                        obj_analysis=data,
                        status_alert="activate-operation",
                    )
                    logging_api(
                        process_log="info", log=f"status_alert: activate-operation | data: {data}")
                
        except Exception as e:
            print(f"***** Erro pré-análise: {e}")
            logging_api(
                        process_log="error", log=f"Error pre-analysis: {e}")
