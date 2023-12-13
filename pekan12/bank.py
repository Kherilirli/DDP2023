class Bank:
    norek = ''
    nama = ''
    saldo = 0
    jmlNasabah = 0
    Bank = 'Bank Syariah Nurul Fikri'

def _init_(self,no,nasabah,saldo):
    self.norek = no
    self.nama = nasabah
    self.saldo = saldo
    Bank.jmlNasabah += 1

def nabung(self,uang):
    self.saldo += uang

def tarik(self, uang):
    self.saldo -= uang

def cetak(self): print(Bank.Bank,
    '\n============================',
    '\nNo. Rekening\t:',self.norek,
    '\nNama Nasabah:',self.nama,
    '\n'
    )   