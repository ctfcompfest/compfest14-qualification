from __future__ import unicode_literals

import re
import sys

charMap = {
    "0": "$#",
    "1": "${##}",
    "2": "$((${##}<<${##}))",
    "3": "$(($((${##}<<${##}))^${##}))",
    "4": "$((${##}<<$((${##}<<${##}))))",
    "5": "$(($((${##}<<$((${##}<<${##}))))^${##}))",
    "6": "$(($(($((${##}<<${##}))^${##}))<<${##}))",
    "7": "$(($(($(($((${##}<<${##}))^${##}))<<${##}))^${##}))"
}

charTemplate = "$\\'\\\\{}\\'"
cmdPrefix = "${!#}<<<"
cmdDelim = "&&"

def encode_cmd(command):
    matches = re.split(r'([&;]+)', command)
    payload = ''

    for match in matches:
        charTemp = ''

        if match == cmdDelim:
            payload += cmdDelim
            continue

        elif re.match('.+\s.+', match):
            cmdTemplate = "{0}{{{1}}}"
            space = True
        else:
            cmdTemplate = '{0}{1}'
            space = False
        
        for char in match.strip():
            if re.match('[A-Za-z0-9]', char):
                octVal = oct(ord(char)).lstrip('-0o')
                charSubs = charTemplate.format(''.join(
                    charMap.get(_) for _ in octVal
                ))

                charTemp += charSubs

            elif re.match('\s', char):
                charTemp += ','
            else:
                if char == '|':
                    charTemp += '}\\' + char + '{'
                else:
                    charTemp += '\\' + char


        payload += cmdTemplate.format(
            cmdPrefix, charTemp
        )

    return payload