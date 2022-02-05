# Projeto de Envio de Mensagem
Enviar mensagem de WhatsApp automatizada via Python

## Instalações
Projeto feito no Spyder (anaconda3):
- no comando `pip install pywhatkit` é necessário o ponto de exclamação antes do comando pip (`!pip`) - dependendo da IDE pode ser que não seja necessário, como o VSCode por exemplo
- no comando `pywhatkit.sendwhatmsg("+5535999999999", "teste", 18, 50)` os argumentos são, respectivamente, o número para qual deseja enviar a mensagem (com o ddi e ddd), a mensagem (teste) e o horário em que a mensagem deve ser enviada (18h 50min)
- para que seja possível o envio da mensagem, o WhatsApp Web deve estar aberto
