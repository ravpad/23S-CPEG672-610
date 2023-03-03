####################################################################################################
# Dec_Hill.py
# Hill2x2 decryption functions
# Written by - Ravi Padma
####################################################################################################
import random
def c2i(character):
  #print('c2i:',ord(character)-ord('a'))
  return ord(character)-ord('A')

def i2c(encoded):
  #print('i2c:',chr(ord('a') + encoded))
  return chr(ord('a') + encoded)

def fitness(sometext):
  score=0
  fitwords= ["the", "of", "and", "to", "in", "is", "you", "that", "there", "it", "he", "she", "was", "for", "on", "are", "as", "with", "his", "they", "at", "be", "this", "have", "from", "if", "were", "their", "him", "her"]

  for word in fitwords:
      score += sometext.count(word)*len(word)
      #print(score)
  return score

def hill_enc(plain):
    found = False
    a=1
    b=1
    c=1
    d=1
    while not found:
        a,b,c,d = [random.randint(0,25) for i in range(4)]
        det = (ad - bc) % 26
        det2 = ((a-1)*d - b*(c-1)) % 26
        if (det % 2 != 0 ) and (det % 13 != 0) and (det2 % 26 != 0):
            found = True
    secret = ''
    for i in range(0, len(plain), 2):
        i1 = c2i(plain[i])
        i2 = c2i(plain[i+1])
        c1 = (i1*a + i2*b) % 26
        c2 = (i1*c + i2*d) % 26
        secret += i2c(c1) + i2c(c2)
    return secret, [a,b,c,d]

def hill_dec(inplain, a,b,c,d):
    secret = ''
    for i in range(0, len(inplain), 2):
        i1 = c2i(inplain[i])
        i2 = c2i(inplain[i+1])
        c1 = (i1*a + i2*b) % 26
        c2 = (i1*c + i2*d) % 26
        secret += i2c(c1) + i2c(c2)
        #secret += c2i(c1) + c2i(c2)
    return secret

CT1='tswenajgdnaxwhswurmdbagkitxuyofqnkormdsrxdlmpkdkxdootvysewdiagkkguzbvqwexdrayqnajqzqtsxdvgtsgqcvqbfeatgqgvdwweuuztxddwakevhhlmqotosokzrufetscxucurdiveuuhzcivtukrdvquhbwvgiaanaxxdlcwgmcvzjekygijitswscocvyffopcxdlmswrdxdwumdhzwklmswrdqragkyewitbamwwezhweqemdklxdxyjgavbaxdgiirqswviraguhvtkzvmjejukyefsfirqszjwgdwtsugxuxdnkoopohygitiurdikbegypfeibhzmgklcopcyvcrtsirelmsbaugywvtbescavoraggnbecoaxkbnpwvdiavhhawatbaytxuaxagkbhzwvezxudikynawlajmdtypdkzitpobonkxdlmziiryhicaxkbapawkpkbqkopicklfecbksyfsfbcjlbonkxdlmziirivryfemqejxuirurtljetiwuzbycrkpdwkseicmdsrcmlkvgeyjicebrgioqcvituxqkdxnkweqrwedicxqfbe'

I=0
bestscor=0
TEXT=CT1.upper()
print(TEXT)
for a in range(26):
  for b in range(26):
    for c in range(26):
      for d in range(26):
        score=fitness(hill_dec(TEXT,a,b,c,d))
        if (a > I):
          I=a
          print (I)
        if (score > bestscor):
          print(score,hill_dec(TEXT, a, b, c, d))
          bestscor=score