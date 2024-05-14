# Snake (mini-projeto)

Esta atividade não é um exercício com testes automáticos. É muito
mais um mini-projeto (talvez, mini-mini-projeto). A ideia é
implementar o famoso jogo da cobrinha cohecido como _snake_
(visite o link abaixo, pra um contexto histórico).

- [Snake na wikipedia](https://en.wikipedia.org/wiki/Snake_video_game)

## Rode os exemplos

Para rodar o `snake` que fizemos em sala de aula, use o comando
`p1-snake` (observe que se muitos estiverem rodando ao mesmo
tempo ou se houver alguma lentidão na rede, você pode perceber
algum delay ou lag na execução; observe que ele está rodando na
VM do worker da disciplina).

No diretório desta atividade, fornecemos também o código básico
de um pequeno projeto que use o `curses`, no arquivo de nome
`exemplo.py`. Rode esse programa e entenda-o. Observe que há
algumas variáveis globais necessárias para a biblioteca `curses`
que são configuradas pela função `main` (`scr` representa a tela
do terminal; `NLINS` o número de linhas da tela; e `NCOLS` o
número de colunas). Observe ainda que o código principal da
lógica em si da aplicação é iniciado na função `exemplo`.


## Implemente seu jogo

Comece com o código fornecido. Sugiro copiar o arquivo para outro
chamado `snake.py`. Assim, você pode deixar o código original do
exemplo intacto. Edite o arquivo `snake.py` e apague a função
`exemplo` e crie a função `snake` (edite o `main` para que
invoque essa nova função, claro). Dentro dessa função escreva a
aplicação _snake_.

Este é um exercício que requer que você trabalhe em etapas.
Decida um pequeno passo que queira fazer e faça apenas esse
passo, sem se preocupar muito com os seguintes. Só depois de
concluir esse passo, você deve pensar em um segundo e assimpor
diante. Cada passo deve deixar você mais próximo do objetivo
final. Mas sempre tenha o seu programa funcionando perfeitamente
a cada passo.

## Projete a estrutura de dados

Comece pensando na estrutura de dados que você usará para
representar os dados do jogo. Lembre que você precisa manter: o
corpo da cobra, a sua velocidade e, se quiser incrementar, a
pontuação do usuário. Pense antes quais dados precisam ser
mantidos e projete as funções necessárias para esses dados: quais
funções criam os dados, quais funções manipulam os dados (quais
alteram, quais lêem, etc). Separe bem as funções que alteram
dados das funções que usam esses dados para desenhar a tela com
base nos dados ou na leitura de dados da entrada. Por fim,
garanta que o programa principal seja uma abstração boa e legível
do que acontece e deve acontecer no programa desde que começa a
executar até o final. O programa deve ser legível. Use funções
(não comentários) para mantê-lo muito legível.


## Leia a documentação do curses

Você precisa de pouca coisa pra fazer um _snake_: `addstr()`,
`refresh()`, `getch()`, `nodelay()` e `getmaxyx()` (que nem é
necessário mesmo, já que é usada no `main` fornecido na
atividade). Você pode também querer usar a função `sleep()` da
biblioteca `time` para fazer _delays_ e tornar o programa usável,
já que pode ficar mais rápido que o apropriado. Por fim, você
pode querer usar a função `randint` da biblioteca `random` para
gerar números aleatórios. Abaixo os links para o curses, caso
queira experimentar alguma outra função.

- [Tutorial](https://docs.python.org/3/howto/curses.html)
- [API](https://docs.python.org/3/library/curses.html)