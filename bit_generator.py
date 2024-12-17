# Импортируем необходимые модули
import io
import binascii

file = open('output_file.rbf', 'rb')
FILESIZE = 200000

data = file.read()
dataLen = len(data);

file.close()
ctr = 0

for filectr in range(dataLen // FILESIZE + 1):

  with open('config{}.h'.format(filectr), 'w') as file:
    file.write('#include <stdint.h>\n uint8_t config [] = {')

  with open('config{}.h'.format(filectr), 'a') as file:
    skip = 1

    for ctr in range(FILESIZE):
      if skip: skip = 0

      else: file.write(', ')

      try:
        file.write(str(data[ctr + FILESIZE * filectr]))
      except IndexError:
        ctr -= 1
        break
    file.write('}};\n#define CONFIG_LEN_CUR {}\n#define CONFIG_LEN_COMMON {}\n#define FULL_CONFIG_LEN {}'.format(ctr + 1, FILESIZE, (dataLen // FILESIZE + 1)))

with open('config_info.h'.format(filectr), 'w') as file:
  file.write('#define CONFIG_LEN_LAST {}\n#define CONFIG_LEN_COMMON {}\n#define FULL_CONFIG_LEN {}\n#define FILE_CONFIG_LEN {}'.format(ctr + 1, FILESIZE, FILESIZE * (dataLen // FILESIZE) + ctr + 1, (dataLen // FILESIZE + 1)))