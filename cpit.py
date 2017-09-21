import sys
import getopt
import random
import logging
import pyperclip
import json, urllib
from sjcl import SJCL
from os.path import expanduser


class Config(object):
  
  def __init__(self, log, config_file='~/.config/cpit.cfg'):
    self.config_file = expanduser(config_file)

  
  def load(self):
    with open(self.config_file) as json_file:
      data = json.load(json_file)
      return data


  def save(self, data):
    with open(self.config_file, 'w') as outfile:
      json.dump(data, outfile)


  def passcode(self, length=32):
    valid_letters='abcdefghijklmnopqrestuvqxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    return ''.join((random.choice(valid_letters) for i in xrange(length)))


def usage_options():
  WHITE = '\033[1m'
  RESET = '\033[0m'
  print ''
  print '\t{0}cpit:{1} '.format(WHITE, RESET)
  print ''
  sys.exit(1)


def establish_logger(level=False):
	logging.basicConfig(format='[%(asctime)s] [%(levelname)s]: %(message)s', datefmt='%d/%m/%Y %I:%M:%S')
	log = logging.getLogger()
	if level is True:
		log.setLevel(logging.DEBUG)
	else:
		log.setLevel(logging.FATAL)
	return log


def copy_from_stdin(log, cfg):
  data = None
  try:
    data = sys.stdin.read()
  except KeyboardInterrupt:
    log.warn('KeyboardInterrupt called, exiting.')
    sys.exit(1)
  log.info('Data copied from stdin.')
  return data


def send_to_server(log, data):
	url = "http://localhost"


def save_to_file(log, cfg, data):
  passcode = cfg.passcode()
  data = SJCL().encrypt(data, passcode)
  log.info('Message [{0}]'.format(data))
  data['passcode'] = passcode
  cfg.save(data)


def get_paste(cfg):
  data = cfg.load()
  data = SJCL().decrypt(data, data['passcode'])
  return data
  

def main(argv):
  log = establish_logger(False)

  try:
    opts, args = getopt.getopt(argv, "?v", ["help", "verbose"])
  except getopt.GetoptError:
    usage_options()

  for opt, arg in opts:
    if opt in ('-?', '--help'):
      usage_options()
    elif opt in ('-f', '--file'):
      filename = arg
    elif opt in ('-v', '--verbose'):
      log = establish_logger(True)

  # Copy from stdin:
  cfg = Config(log)
  if sys.stdin.isatty() is False:
    data = copy_from_stdin(log, cfg)
    pyperclip.copy(data)
    data = save_to_file(log, cfg, data)
  else:
    print get_paste(cfg)


if __name__ == "__main__":
  main(sys.argv[1:])

