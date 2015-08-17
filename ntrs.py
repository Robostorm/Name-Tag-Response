import main, sys
from daemon import Daemon

class NTDaemon(Daemon):
    def run(self):
        main.start()

if __name__ == '__main__':
    daemon = NTDaemon('/tmp/ntdaemon.pid', stdout='/var/log/ntrout.log', stderr='/var/log/ntrerr.log')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            print "Staring Name Tag Response Server..."
            daemon.start()
        elif 'stop' == sys.argv[1]:
            print "Stopping Name Tag Response Server..."
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            print "Restarting Name Tag Response Server..."
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)