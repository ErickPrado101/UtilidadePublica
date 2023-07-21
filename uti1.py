import win32com.client as win32

# lista com os endereços de e-mail dos destinatários
dest = []
email = win32.Dispatch ('email.application')

nemail = email.CreatItem(0)
destinatarios_str = ";".join(dest)

email.To = destinatarios_str
email.Subject = ""
email.HTMLNody = " "

anex = "C/..."
email.Attachments.Add(anex)

email.Send()
print("E-mail enviado com sucesso")
