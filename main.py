from processor.dataprocessor_service import DataProcessorService

"""
    Main-модуль, т.е. модуль запуска приложений ("точка входа" приложения)
"""

if __name__ == '__main__':
    service_1 = DataProcessorService(datasource="doctor.csv", db_connection_url="sqlite:///yoru.db")
    service_1.run_service()

    service_2 = DataProcessorService(datasource="patient.csv", db_connection_url="sqlite:///yoru.db")
    service_2.run_service()

    service_3 = DataProcessorService(datasource="appointment.csv", db_connection_url="sqlite:///yoru.db")
    service_3.run_service()
