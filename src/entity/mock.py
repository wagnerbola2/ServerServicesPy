import win32service

def getMockServices():
  return [
    ('auth', '01.00.01 - Servico | Auth', (16, win32service.SERVICE_RUNNING, 449, 0, 0, 0, 0)),
	  ('bancoDados', '01.01.01 - Servico | BancoDados', (16, win32service.SERVICE_RUNNING, 1, 0, 0, 0, 0)),
	  ('master', '01.02.01 - Servico | Master', (16, win32service.SERVICE_RUNNING, 449, 0, 0, 0, 0)),
	  ('slave1', '01.03.01 - Servico | Slave1', (16, win32service.SERVICE_RUNNING, 449, 0, 0, 0, 0)),
	  ('slave2', '01.03.02 - Servico | Slave2', (16, win32service.SERVICE_RUNNING, 449, 0, 0, 0, 0)),
	  ('slave3', '01.03.03 - Servico | Slave3', (16, win32service.SERVICE_RUNNING, 449, 0, 0, 0, 0)),
	  ('slave4', '01.03.04 - Servico | Slave4', (16, win32service.SERVICE_STOPPED, 449, 0, 0, 0, 0)),
	  ('slave5', '01.03.05 - Servico | Slave5', (16, win32service.SERVICE_STOPPED, 449, 0, 0, 0, 0)),
	  ('Rest', '01.05.01 - Servico | Api Rest', (16, win32service.SERVICE_RUNNING, 449, 0, 0, 0, 0))
	  ('Soap', '01.05.02 - Servico | Api Soap', (16, win32service.SERVICE_STOPPED, 449, 0, 0, 0, 0))
	  ('Schedule', '01.06.01 - Servico | Schedule', (16, win32service.SERVICE_RUNNING, 449, 0, 0, 0, 0))
  ]