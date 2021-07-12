import mailparser
import argparse

# mail = mailparser.parse_from_bytes(byte_mail)
# mail = mailparser.parse_from_file(f)
# mail = mailparser.parse_from_file_msg(outlook_mail)
# mail = mailparser.parse_from_file_obj(fp)
# mail = mailparser.parse_from_string(raw_mail)


mail_content_types = ['image/jpeg', 'text/plain', 'application/vnd.ms-excel']


def parse():
    parser = argparse.ArgumentParser(description='Please enter file path')
    parser.add_argument('file', metavar="FILE", help='please enter the file path', type=str)
    args = parser.parse_args()
    return args


def get_attachment():
    args = parse()
    source_file = args.file
    mail = mailparser.parse_from_file(source_file)
    attachment = mail.attachments
    print(attachment)
    return attachment, mail


def download_attachment():
    destination = "file path"
    attachment, mail = get_attachment()
    for value in attachment:
        content_type = value['mail_content_type']
        print(value)
        if content_type == mail_content_types[1]:
            mail.write_attachments(destination)
            print("attachment successfully saved..")
        else:
            print("this is not a text file, unable to save")


if __name__ == "__main__":
    get_attachment()
    download_attachment()