import win32service

def getMockServices():
  return [("LicenseServer", "01.01.01 - TOTVS | License Server", (16, win32service.SERVICE_RUNNING, 0)),
            ("tp12_dbAcess", "01.02.01 - TOTVS | Db Acess", (16, win32service.SERVICE_RUNNING, 0)),
            ("tp12_master", "01.03.01 - TOTVS | Master", (16, win32service.SERVICE_RUNNING, 0)),
            ("tp12_salve1", "01.03.02 - TOTVS | Slave1", (16, win32service.SERVICE_RUNNING, 0)),
            ("tp12_salve2", "01.03.03 - TOTVS | Slave2", (16, win32service.SERVICE_RUNNING, 0)),
            ("tp12_salve3", "01.03.04 - TOTVS | Slave3", (16, win32service.SERVICE_RUNNING, 0)),
            ("tp12_salve4", "01.03.05 - TOTVS | Slave4", (16, win32service.SERVICE_STOPPED, 0)),
            ("tp12_salve5", "01.03.06 - TOTVS | Slave5", (16, win32service.SERVICE_STOPPED, 0)),
            ("tp12_WsRest", "01.04.01 - TOTVS | WS REST", (16, win32service.SERVICE_RUNNING, 0)),
            ("tp12_WsSoap", "01.04.02 - TOTVS | WS Soap", (16, win32service.SERVICE_STOPPED, 0)),
            ("tp12_Schedule", "01.05.01 - TOTVS | Schedule", (16, win32service.SERVICE_RUNNING, 0)),
            ]