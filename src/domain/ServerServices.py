from src.entity.envioment import envioment
from src.entity.mock import getMockServices
import win32con
import win32service

class ServerServices:
    def __init__(self):
        self.envioment = envioment()
        server = self.envioment.server
        accessSCM = win32con.GENERIC_READ
        # self.hscm = win32service.OpenSCManager(server, None, accessSCM)
        self.typeFilter = win32service.SERVICE_WIN32
        self.stateFilter = win32service.SERVICE_STATE_ALL

    def getServices(self):
        # services = win32service.EnumServicesStatus(self.hscm, self.typeFilter, self.stateFilter)
        services = getMockServices()
        servicesFiltred = self.filterServices(services, "TOTVS")
        servicesParsed = self.parseStatusServices(servicesFiltred)
        return servicesParsed
    
    def filterServices(self, services, filterText):
        self.filterText = filterText
        def filterTotvs(service, filterText):
            _, desc, *_ = service
            return filterText in desc
        totvsServices = list(filter(lambda x: filterTotvs(x, filterText=filterText), services))
        return self.sortTotvServices(totvsServices)
    
    def sortTotvServices(self, services):
        return sorted(services, key=lambda service: service[1])
    
    def parseStatusServices(self, services):
        servicesParsed = [] 
        for (short_name, desc, status) in services:
            _, codeStatus, *_ = status
            descStatus = self.getServiceStatus(codeStatus)
            servicesParsed.append((short_name, desc, descStatus))
        return servicesParsed

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