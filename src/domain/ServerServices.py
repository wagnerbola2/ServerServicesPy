from src.entity.envioment import envioment
import win32con
import win32service

class ServerServices:
    def __init__(self):
        self.envioment = envioment()
        server = self.envioment.server
        accessSCM = win32con.GENERIC_READ
        self.hscm = win32service.OpenSCManager(server, None, accessSCM)
        self.typeFilter = win32service.SERVICE_WIN32
        self.stateFilter = win32service.SERVICE_STATE_ALL

    def getServices(self):
        services = win32service.EnumServicesStatus(self.hscm, self.typeFilter, self.stateFilter)
        totvsServices = self.filterTotvServices(services)
        for (short_name, desc, status) in totvsServices:
            _, codeStatus, *_ = status
            descStatus = self.getServiceStatus(codeStatus)
            print(short_name, desc, descStatus)
    
    def filterTotvServices(self, services):
        def filterTotvs(service):
            _, desc, *_ = service
            return "TOTVS" in desc
        totvsServices = list(filter(filterTotvs, services))
        return self.sortTotvServices(totvsServices)
    
    def sortTotvServices(self, services):
        return sorted(services, key=lambda service: service[1])
    
    def getServiceStatus(self, codeStatus):
        match codeStatus:
            case win32service.SERVICE_STOPPED:
                descStatus = "STOPPED"
            case win32service.SERVICE_STOP_PENDING:
                descStatus = "STOP PENDING"
            case win32service.SERVICE_RUNNING:
                descStatus = "RUNNING"
            case win32service.SERVICE_START_PENDING:
                descStatus = "START_PENDING"
        return descStatus