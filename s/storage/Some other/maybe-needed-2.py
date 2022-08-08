Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for n in range(10_000):
	# if sqrt(a := n*(n+1))**2 == a
	pass

>>> def is_square(n, *, eps=1e-8):
	return int(sqrt(n) + eps)**2 == n

>>> for n in range(10_000):
	# if sqrt(a := n*(n+1))**2 == a
	if is_square(n*(n+1)/3):
		print(n)

		
Traceback (most recent call last):
  File "<pyshell#9>", line 3, in <module>
    if is_square(n*(n+1)/3):
  File "<pyshell#6>", line 2, in is_square
    return int(sqrt(n) + eps)**2 == n
NameError: name 'sqrt' is not defined
>>> for n in range(10_000):
	# if sqrt(a := n*(n+1))**2 == a
	if is_square(n*(n+1)/3):
		print(n)
KeyboardInterrupt
>>> from math import sqrt
>>> for n in range(10_000):
	# if sqrt(a := n*(n+1))**2 == a
	if is_square(n*(n+1)/3):
		print(n)

		
0
3
48
675
9408
>>> for n in range(100_000):
	# if sqrt(a := n*(n+1))**2 == a
	if is_square(n*(n+1)/3):
		print(n)

		
0
3
48
675
9408
>>> for n in range(1_000_000):
	# if sqrt(a := n*(n+1))**2 == a
	if is_square(n*(n+1)/3):
		print(n)

		
0
3
48
675
9408
131043
>>> for n in range(20_000_000):
	# if sqrt(a := n*(n+1))**2 == a
	if is_square(n*(n+1)/3):
		print(n)

		
0
3
48
675
9408
131043
1825200
>>> for n in range(20_000_000, 40_000_000 + 1):
	if is_square(n*(n+1)/3):
		print(n)

		
25421763
>>> def main(range_):
	for n in range_:
		if is_square(n*(n+1)/3):
			print(n)

			
>>> main(40_)
SyntaxError: invalid decimal literal
>>> def main(range_):
	for n in range_:
		if is_square(n*(n+1)/3):
			print(n)

			
>>> main(1, 40_000_000 + 1)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    main(1, 40_000_000 + 1)
TypeError: main() takes 1 positional argument but 2 were given
>>> main(range(1, 40_000_000 + 1))
3
48
675
9408
131043
1825200
25421763
>>> # --- Part
>>> some_answers = []
>>> lst = list(eval("""
3
48
675
9408
131043
1825200
25421763
""".replace('\n', ',')))
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    lst = list(eval("""
  File "<string>", line 1
    ,3,48,675,9408,131043,1825200,25421763,
    ^
SyntaxError: invalid syntax
>>> some_answers = []
>>> lst = list(eval("""\
3
48
675
9408
131043
1825200
25421763
""".replace('\n', ',')))
>>> some_answers.extend(lst)
>>> some_answers
[3, 48, 675, 9408, 131043, 1825200, 25421763]
>>> from time import time  # For some measuring
>>> def one_action():
	t0 = time()
	last_received_answer = some_answers[-1]
	i = last_received_answer * 13:
		
SyntaxError: invalid syntax
>>> some_answers = []
>>> lst = list(eval("""\
3
48
675
9408
131043
1825200
25421763
""".replace('\n', ',')))
>>> some_answers.extend(lst)
>>> some_answers
[3, 48, 675, 9408, 131043, 1825200, 25421763]
>>> from time import time  # For some measuring
>>> def one_action():
	t0 = time()
	last_received_answer = some_answers[-1]
	i = last_received_answer * 13
	while True:
		if is_square(n*(n+1)/3):
			break
	nonlocal some_answers
	
SyntaxError: name 'some_answers' is used prior to nonlocal declaration
>>> some_answers = []
>>> lst = list(eval("""\
3
48
675
9408
131043
1825200
25421763
""".replace('\n', ',')))
>>> some_answers.extend(lst)
>>> some_answers
[3, 48, 675, 9408, 131043, 1825200, 25421763]
>>> from time import time  # For some measuring
>>> def one_action(k=13):
	nonlocal some_answers
	t0 = time()
	last_received_answer = some_answers[-1]
	n = last_received_answer * k
	while True:
		if is_square(n*(n+1)/3):
			break
	print(f"Wasted time: {time() - t0}")
	some_answers.append(n)
	
SyntaxError: no binding for nonlocal 'some_answers' found
>>> def one_action():
	t0 = time()
	last_received_answer = some_answers[-1]
	i = last_received_answer * 13
	while True:
		if is_square(n*(n+1)/3):
			break
	global some_answers
	
SyntaxError: name 'some_answers' is used prior to global declaration
>>> some_answers = []
>>> lst = list(eval("""\
3
48
675
9408
131043
1825200
25421763
""".replace('\n', ',')))
>>> some_answers.extend(lst)
>>> some_answers
[3, 48, 675, 9408, 131043, 1825200, 25421763]
>>> from time import time  # For some measuring
>>> def one_action(k=13):
	global some_answers
	t0 = time()
	last_received_answer = some_answers[-1]
	n = last_received_answer * k
	while True:
		if is_square(n*(n+1)/3):
			break
	print(f"Wasted time: {time() - t0}")
	some_answers.append(n)
	return n

>>> one_action(k=13)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    one_action(k=13)
  File "<pyshell#69>", line 7, in one_action
    if is_square(n*(n+1)/3):
KeyboardInterrupt
>>> # More then 15 minutes went...
>>> def one_action(k=13, max_k=15):
	global some_answers
	t0 = time()
	last_received_answer = some_answers[-1]
	n = last_received_answer * k
	maxn = last_reveived_answer * max_k
	while n < maxn and not is_square(n*(n+1)/3):
		n += 1
	if not is_square(n*(n+1)/3):
		raise Exception("Wow! not found in that bounds.")
	print(f"Wasted time: {time() - t0}")
	some_answers.append(n)
	return n

>>> del some_answers[-1]
>>> some_answers
[3, 48, 675, 9408, 131043, 1825200]
>>> one_action()
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    one_action()
  File "<pyshell#73>", line 6, in one_action
    maxn = last_reveived_answer * max_k
NameError: name 'last_reveived_answer' is not defined
>>> def one_action(k=13, max_k=15):
	global some_answers
	t0 = time()
	last_received_answer = some_answers[-1]
	n = last_received_answer * k
	maxn = last_received_answer * max_k
	while n < maxn and not is_square(n*(n+1)/3):
		n += 1
	if not is_square(n*(n+1)/3):
		raise Exception("Wow! not found in that bounds.")
	print(f"Wasted time: {time() - t0}")
	some_answers.append(n)
	return n

>>> one_action()
Wasted time: 4.082667589187622
25421763
>>> one_action(k=13, max_k=15)
Wasted time: 74.18577599525452
354079488
>>> one_action(k=13.92820-0.01, max_k=13.92820+0.01)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    one_action(k=13.92820-0.01, max_k=13.92820+0.01)
  File "<pyshell#78>", line 10, in one_action
    raise Exception("Wow! not found in that bounds.")
Exception: Wow! not found in that bounds.
>>> one_action(k=13.92820-0.1, max_k=13.92820+0.1)
Wasted time: 107.7826771736145
4928508448.9616
>>> some_answers
[3, 48, 675, 9408, 131043, 1825200, 25421763, 354079488, 4928508448.9616]
>>> is_square(4928508448)
False
>>> is_square(4928508448-1)
False
>>> is_square(4928508448+1)
False
>>> # one_action(k=13.92820-0.1, max_k=13.92821+0.1)
>>> def one_action(k=13, max_k=15):
	global some_answers
	t0 = time()
	last_received_answer = some_answers[-1]
	n = int(last_received_answer * k)
	maxn = last_received_answer * max_k
	while n < maxn and not is_square(n*(n+1)/3):
		n += 1
	if not is_square(n*(n+1)/3):
		raise Exception("Wow! not found in that bounds.")
	print(f"Wasted time: {time() - t0}")
	some_answers.append(n)
	return n

>>> is_square(25421763)
False
>>> list(filter, lambda i: not is_square(i), some_answers)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    list(filter, lambda i: not is_square(i), some_answers)
TypeError: list expected at most 1 argument, got 3
>>> list(filter(lambda i: not is_square(i), some_answers))
[3, 48, 675, 9408, 131043, 1825200, 25421763, 354079488, 4928508448.9616]
>>> list(filter(lambda i: not is_square(3*i*(i+1)), some_answers))
[4928508448.9616]
>>> one_action(k=13.92819, max_k=13.92821)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    one_action(k=13.92819, max_k=13.92821)
  File "<pyshell#89>", line 10, in one_action
    raise Exception("Wow! not found in that bounds.")
Exception: Wow! not found in that bounds.
>>> one_action(k=13.928100, max_k=13.928204)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    one_action(k=13.928100, max_k=13.928204)
  File "<pyshell#89>", line 10, in one_action
    raise Exception("Wow! not found in that bounds.")
Exception: Wow! not found in that bounds.
>>> one_action(k=13.928000, max_k=13.928000)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    one_action(k=13.928000, max_k=13.928000)
  File "<pyshell#89>", line 10, in one_action
    raise Exception("Wow! not found in that bounds.")
Exception: Wow! not found in that bounds.
>>> some_answers
[3, 48, 675, 9408, 131043, 1825200, 25421763, 354079488, 4928508448.9616]
>>> del some_answers[-1]
>>> one_action(k=13.928100, max_k=13.928204)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    one_action(k=13.928100, max_k=13.928204)
  File "<pyshell#89>", line 10, in one_action
    raise Exception("Wow! not found in that bounds.")
Exception: Wow! not found in that bounds.
>>> some_answers
[3, 48, 675, 9408, 131043, 1825200, 25421763, 354079488]
>>> 354079488*(354079488 + 1)*3
376116852529264896
>>> one_action(k=13.928100, max_k=14.0)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    one_action(k=13.928100, max_k=14.0)
  File "<pyshell#89>", line 10, in one_action
    raise Exception("Wow! not found in that bounds.")
Exception: Wow! not found in that bounds.
>>> one_action(k=13.928000, max_k=13.928500)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    one_action(k=13.928000, max_k=13.928500)
  File "<pyshell#89>", line 10, in one_action
    raise Exception("Wow! not found in that bounds.")
Exception: Wow! not found in that bounds.
>>> one_action(k=13.90000, max_k=13.928500)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    one_action(k=13.90000, max_k=13.928500)
  File "<pyshell#89>", line 10, in one_action
    raise Exception("Wow! not found in that bounds.")
Exception: Wow! not found in that bounds.
>>> one_action(k=13.80000, max_k=14)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    one_action(k=13.80000, max_k=14)
  File "<pyshell#89>", line 10, in one_action
    raise Exception("Wow! not found in that bounds.")
Exception: Wow! not found in that bounds.
>>> def one_action(k=13, max_k=15):
	global some_answers
	t0 = time()
	last_received_answer = some_answers[-1]
	n = int(last_received_answer * k)
	maxn = last_received_answer * max_k
	# Note: Here "/3" is similar to "*3".
	while not is_square(n*(n+1)*3) and n <= maxn:
		n += 1
	print(f"Wasted time: {time() - t0}")
	if not is_square(n*(n+1)*3):
		raise Exception("Wow! not found in that bounds.")
	some_answers.append(n)
	return n

>>> one_action(k=13.92000, max_k=14)
Wasted time: 8.903794527053833
4931691075
>>> is_square(4931691075*(4931691075+1)/3)
False
>>> is_square(4931691075*(4931691075+1)*3)
True
>>> one_action(k=13.928203248531585*0.99, max_k=14)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    one_action(k=13.928203248531585*0.99, max_k=14)
  File "<pyshell#107>", line 8, in one_action
    while not is_square(n*(n+1)*3) and n <= maxn:
  File "<pyshell#6>", line 2, in is_square
    return int(sqrt(n) + eps)**2 == n
KeyboardInterrupt
>>> one_action(k=13.92820, max_k=14)
Wasted time: 0.04399275779724121
68689595568
>>> one_action(k=13.928203, max_k=14)  # Here that `k` digits were so on some last comutations.
Wasted time: 0.043970346450805664
956722646883
>>> one_action(k=13.9282032, max_k=14)  # Here that `k` digits were so on some last comutations.
Wasted time: 0.08400106430053711
13325427460800
>>> one_action(k=13.928203230, max_k=14)  # Here that `k` digits were so on some last comutations.
Wasted time: 0.009969949722290039
185599261804323
>>> one_action(k=13.928203230, max_k=14)  # Here that `k` digits were so on some last comutations.
Wasted time: 0.14490437507629395
2585064237799728
>>> one_action(k=13.928203230275, max_k=14)  # Here that `k` digits were so on some last comutations.

>>> one_action(k=13.92820323027, max_k=14)  # Here that `k` digits were so on some last comutations.

>>> 
one_action(k=13.928203230, max_k=13.9283)
>>> one_action(k=13.92820323025, max_k=13.92820323030)
Wasted time: 0.4820065498352051

>>> one_action(k=13.92820323000, max_k=13.92820323100)
Wasted time: 9.037713766098022
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    one_action(k=13.92820323000, max_k=13.92820323100)
  File "<pyshell#107>", line 12, in one_action
    raise Exception("Wow! not found in that bounds.")
Exception: Wow! not found in that bounds.
>>> one_action(k=14.0 - 1e-10, max_k=14 + 1e-10)
Wasted time: 1.767256736755371
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    one_action(k=14.0 - 1e-10, max_k=14 + 1e-10)
  File "<pyshell#107>", line 12, in one_action
    raise Exception("Wow! not found in that bounds.")
Exception: Wow! not found in that bounds.
>>> one_action(k=14, max_k=14 + 1e-8)
Wasted time: 91.81615996360779
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    one_action(k=14, max_k=14 + 1e-8)
  File "<pyshell#107>", line 12, in one_action
    raise Exception("Wow! not found in that bounds.")
Exception: Wow! not found in that bounds.
>>> one_action(k=14 + 1e-8 - 1e-10, max_k=14 + 2e-8)
Wasted time: 91.40288639068604
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    one_action(k=14 + 1e-8 - 1e-10, max_k=14 + 2e-8)
  File "<pyshell#107>", line 12, in one_action
    raise Exception("Wow! not found in that bounds.")
Exception: Wow! not found in that bounds.
>>> one_action(k=14 + 2e-8 - 1e-10, max_k=14 + 3e-8)
Wasted time: 90.06130981445312
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    one_action(k=14 + 2e-8 - 1e-10, max_k=14 + 3e-8)
  File "<pyshell#107>", line 12, in one_action
    raise Exception("Wow! not found in that bounds.")
Exception: Wow! not found in that bounds.
>>> for i in range(33605835091396464, 36190899329196192 + 1):
	if is_square(3*i*(i+1), eps=1e-12):
		print()

		
Traceback (most recent call last):
  File "<pyshell#129>", line 2, in <module>
    if is_square(3*i*(i+1), eps=1e-12):
  File "<pyshell#6>", line 2, in is_square
    return int(sqrt(n) + eps)**2 == n
KeyboardInterrupt
>>> def is_square(n):  # New def.
	_k = int(sqrt(n)) - 2
	while (_k+1) ** 2 < n:
		_k += 1
	return (_k+1) ** 2 == n

>>> def is_square(n):  # New def.
	_k = int(sqrt(n)) - 10  # It can be too much...
	while (_k+1) ** 2 < n:
		_k += 1
	return (_k+1) ** 2 == n

>>> one_action(k=13.92820323027, max_k=13.92820323028)
Wasted time: 0.19298171997070312
36005300067391875
>>> is_square(36005300067391875*(36005300067391875+1)*3)
True
>>> one_action(k=13.928203230275, max_k=13.928203230276)
Wasted time: 0.516021728515625
501489136705686528
>>> 501489136705686528/36005300067391875
13.928203230275509
>>> one_action(k=13.9282032302755, max_k=13.9282032302756)
Wasted time: 13.691025495529175
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    one_action(k=13.9282032302755, max_k=13.9282032302756)
  File "<pyshell#107>", line 12, in one_action
    raise Exception("Wow! not found in that bounds.")
Exception: Wow! not found in that bounds.
>>> one_action(k=13.9282032302754, max_k=13.9282032302756)
Wasted time: 27.758485794067383
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    one_action(k=13.9282032302754, max_k=13.9282032302756)
  File "<pyshell#107>", line 12, in one_action
    raise Exception("Wow! not found in that bounds.")
Exception: Wow! not found in that bounds.
>>> one_action(k=13.928203230275, max_k=13.928203230276)
Wasted time: 143.6374213695526
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    one_action(k=13.928203230275, max_k=13.928203230276)
  File "<pyshell#107>", line 12, in one_action
    raise Exception("Wow! not found in that bounds.")
Exception: Wow! not found in that bounds.
>>> some_answers
[3, 48, 675, 9408, 131043, 1825200, 25421763, 354079488, 4931691075, 68689595568, 956722646883, 13325427460800, 185599261804323, 2585064237799728, 36005300067391875, 501489136705686528]
>>> one_action(k=13.92820323027, max_k=13.928203230276)
KeyboardInterrupt
>>> one_action(k=13.928203230275500, max_k=13.928203230275512)
Wasted time: 1.1188054084777832
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    one_action(k=13.928203230275500, max_k=13.928203230275512)
  File "<pyshell#107>", line 12, in one_action
    raise Exception("Wow! not found in that bounds.")
Exception: Wow! not found in that bounds.
>>> one_action(k=13.928203230275000, max_k=13.928203230275512)
Wasted time: 60.91456079483032
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    one_action(k=13.928203230275000, max_k=13.928203230275512)
  File "<pyshell#107>", line 12, in one_action
    raise Exception("Wow! not found in that bounds.")
Exception: Wow! not found in that bounds.
>>> 
