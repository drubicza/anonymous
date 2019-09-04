import os, sys
print '\x1b[1;32mLOGIN DULU YA BOZ:v'
print '\x1b[5;33mJIKA TIDAK TAU USER AND PASS NYA SILAHKAN HUBUNGI CHANNEL SAYA'
print 'NAMA CHANNEL : ENTUP ID'
username = 'Nanang'
password = 'ENTUP ID'

def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)


def main():
    uname = raw_input('username : ')
    if uname == username:
        pwd = raw_input('password : ')
        if pwd == password:
            print '\x1b[5;34m[!]LOGIN BERHASIL',
            sys.exit()
        else:
            print '\x1b[1;32mMaaf Masukkan password Anda salah... [?]\x1b[00m'
            print 'Silahkan segera log-in kembali...!!\n'
            restart()
    else:
        print '\x1b[1;32mMaaf Masukkan Username Anda salah... [?]\x1b[00m'
        print 'Silahkan segera log-in kembali...!!\n'
        restart()


try:
    main()
except KeyboardInterrupt:
    os.system('clear')
    restart()
