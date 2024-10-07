from src.entity.envioment import envioment
from src.entity.mock import getMockServices
from config import servers
import win32con
import win32service

class ServerServices:
    def __init__(self, server):
        self.serverConfig = next((e for e in servers if e["server"] == server), None)
        self.erro = None
        if self.serverConfig == None:
            self.erro = "Nenhuma configuração de Servidor foi encontrada"
        accessSCM = win32con.GENERIC_READ
        self.hscm = win32service.OpenSCManager(server, None, accessSCM)
        self.typeFilter = win32service.SERVICE_WIN32
        self.stateFilter = win32service.SERVICE_STATE_ALL

    def getServices(self):
        services = win32service.EnumServicesStatus(self.hscm, self.typeFilter, self.stateFilter)
        # services = getMockServices()
        servicesFiltred = self.filterServices(services, "")
        servicesParsed = self.parseStatusServices(servicesFiltred)
        servicesSorted = self.sortTotvServices(servicesParsed)
        return servicesSorted
    
    def filterServices(self, services, filterText=""):
        serverConfigservices = self.serverConfig["services"]
        def filterTotvs(service, filterText):
            serviceid, *_ = service
            serviceConfig = next((e for e in serverConfigservices if e["id"] == serviceid), None)
            if not serviceConfig:
                return False
            else:
                return True
        totvsServices = list(filter(
            lambda x: filterTotvs(x, filterText=filterText),
            services
        ))
        return totvsServices
    
    def sortTotvServices(self, services):
        return sorted(services, key=lambda service: service[3])
    
    def parseStatusServices(self, services):
        serverConfigservices = self.serverConfig["services"]
        servicesParsed = [] 
        for (short_name, desc, status) in services:
            _, codeStatus, *_ = status
            serviceConfig = next((e for e in serverConfigservices if e["id"] == short_name), None)
            descStatus = self.getServiceStatus(codeStatus)
            servicesParsed.append((short_name, serviceConfig["description"], descStatus, serviceConfig["order"]))
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