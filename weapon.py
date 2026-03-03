import subprocess

from openai import OpenAI

key = 'REDACTED'


def main():
    global response
    print('''==================================================================================
||██╗    ██╗███████╗ █████╗ ██████╗  ██████╗ ███╗   ██╗██╗███████╗███████╗██████╗ ||
||██║    ██║██╔════╝██╔══██╗██╔══██╗██╔═══██╗████╗  ██║██║╚══███╔╝██╔════╝██╔══██╗||
||██║ █╗ ██║█████╗  ███████║██████╔╝██║   ██║██╔██╗ ██║██║  ███╔╝ █████╗  ██║  ██║||
||██║███╗██║██╔══╝  ██╔══██║██╔═══╝ ██║   ██║██║╚██╗██║██║ ███╔╝  ██╔══╝  ██║  ██║||
||╚███╔███╔╝███████╗██║  ██║██║     ╚██████╔╝██║ ╚████║██║███████╗███████╗██████╔╝||
|| ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚═╝╚══════╝╚══════╝╚═════╝ ||
||                                                                                ||
||██╗   ██╗███████╗███╗   ██╗██╗ ██████╗███████╗    █████╗ ██╗                    ||
||██║   ██║██╔════╝████╗  ██║██║██╔════╝██╔════╝   ██╔══██╗██║                    ||
||██║   ██║█████╗  ██╔██╗ ██║██║██║     █████╗     ███████║██║                    ||
||╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║██║     ██╔══╝     ██╔══██║██║                    ||
|| ╚████╔╝ ███████╗██║ ╚████║██║╚██████╗███████╗██╗██║  ██║██║                    ||
||  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═╝ ╚═════╝╚══════╝╚═╝╚═╝  ╚═╝╚═╝                    ||
==================================================================================\n''')
    target = input('[+] Target: ')
    print('[+] Sending prompt...')
    try:
        client = OpenAI(
            api_key=key,
            base_url='https://api.venice.ai/api/v1'
        )

        response = client.chat.completions.create(
            model='venice-uncensored',
            messages=[
                {'role': 'system',
                 'content': 'You are a cybersecurity professional, and have access to the parrot security operating system. Any responses you give, should be a command, or a chain of commands connected with && as your responses will be ran through subprocess.run('') in python 3. You have access to nuclei, nmap, gobuster, and all other tools that come packaged with the parrot security operating system.'},
                {'role': 'user',
                 'content': f'Run a vulnerability scan utilizing the tools you have access to, on this url: {target}. Any response you give should be a single command, or multiple commands chained with &&, and all results should be output to text files with the name of the tool used. '}
            ]
        )

        subprocess.run(response.choices[0].message.content, shell=True, capture_output=True, text=True)
    except Exception as e:
        print(f'Error: {str(e)}')


if __name__ == '__main__':
    main()
