# =============================================================================
# Sestavljanje verig vozlov
#
# Za spodnje naloge morate uvoziti vse definicije iz naloge _Veriga vozlov_.
# To storite z:
# 
#     from veriga_vozlov import Vozel, dodaj_na_konec, dodaj_na_zacetek, vrni_seznam, iz_seznama
# =====================================================================@029182=
# 1. podnaloga
# Sestavite funkcijo `stevilska_veriga(a, b)`, ki vrne referenco na prvi vozel
# v verigi, ki zaporedoma vsebuje števila od `a` do `b`. Predpostavite, da
# velja `a <= b`. Zgled:
# 
#     >>> v = stevilska_veriga(3, 7)
#     >>> v.vrni_seznam()
#     [3, 4, 5, 6, 7]
# =============================================================================
from veriga_vozlov import Vozel, dodaj_na_konec, dodaj_na_zacetek, vrni_seznam, iz_seznama

def stevilska_veriga(a, b):
    v = Vozel(a)
    while a < b:
        a += 1
        dodaj_na_konec(v, a)
    return v

# =====================================================================@029183=
# 2. podnaloga
# Sestavite funkcijo `sodi_in_lihi(v)`, ki kot argument prejme referenco na
# vozel ter vrne dve verigi, ki jih dobi tako, da v eno zloži vozle, ki
# vsebujejo sode podatke, v drugo pa vozle, ki vsebujejo lihe podatke. Funkcija
# naj vrne par in sicer referenci na začetna vozla v obeh verigah. Na primer:
# 
#     >>> v = iz_seznama([7, 5, 2, 1, 3, 4, 9, 8])
#     >>> v1, v2 = sodi_in_lihi(v)
#     >>> v1.vrni_seznam()
#     [2, 4, 8]
#     >>> v2.vrni_seznam()
#     [7, 5, 1, 3, 9]
# =============================================================================

# def sodi_in_lihi(v):
#     s = 0
#     l = 0
#     while v.naslednji is not None:
#         print(v.podatek)
#         if v.podatek % 2 == 0:
#             if s == 0:
#                 v1 = Vozel(v.podatek)
#             else:
#                 dodaj_na_konec(v1, v.podatek)
#             s += 1
#         else:
#             if l == 0:
#                 v2 = Vozel(v.podatek)
#             else:
#                 dodaj_na_konec(v2, v.podatek)
#             l += 1
#         v = v.naslednji
#     return v1, v2

def sodi_in_lihi(v):
    v1 = None
    v2 = None
    while v.naslednji is not None:
        if v.podatek % 2 == 0:
            v1 = dodaj_na_konec(v1, v.podatek)
        else:
            v2 = dodaj_na_konec(v2, v.podatek)
        v = v.naslednji
    if v.podatek % 2 == 0:
        v1 = dodaj_na_konec(v1, v.podatek)
    else:
        v2 = dodaj_na_konec(v2, v.podatek)
    return v1, v2


# =====================================================================@029184=
# 3. podnaloga
# Sestavite funkcijo `podvoji_verigo(prvi)`, ki naj sestavi in vrne novo,
# identično kopijo verige, stare pa naj ne spreminja. Zgled:
# 
#     >>> v = iz_seznama([2, 3, 4, 5])
#     >>> v2 = podvoji_verigo(v)
#     >>> v2.podatek = 11
#     >>> vrni_seznam(v)
#     [2, 3, 4, 5]
#     >>> v2.vrni_seznam(v)
#     [11, 3, 4, 5]
# =============================================================================

def podvoji_verigo(prvi):
    if prvi is None:
        return None
    else:
        v = Vozel(prvi.podatek)
        while prvi.naslednji is not None:
            prvi = prvi.naslednji
            dodaj_na_konec(v, prvi.podatek)
    return v

# =====================================================================@029185=
# 4. podnaloga
# Sestavite funkcijo `stakni_verigi(v1, v2)`, ki kot argumenta prejme referenci
# na dva vozla in sestavi _novo verigo_, ki jo dobi tako, da stakne obe verigi.
# Na primer:
# 
#     >>> v1 = iz_seznama([1, 2, 3])
#     >>> v2 = iz_seznama([4, 5, 6])
#     >>> v = stakni_verigi(v1, v2)
#     >>> v.vrni_seznam()
#     [1, 2, 3, 4, 5, 6]
# =============================================================================

# def stakni_verigi(v1, v2):
#     v = None
#     while v1.naslednji is not None and v2.naslednji is not None:
#         if v1.podatek < v2.podatek:
#             v = dodaj_na_konec(v, v1.podatek)
#             v1 = v1.naslednji
#         else:
#             v = dodaj_na_konec(v, v2.podatek)
#             v2 = v2.naslednji
#     while v1.naslednji is None and v2.podatek < v1.podatek:
#         v = dodaj_na_konec(v, v2.podatek)
#         v2 = v2.naslednji
#     v = dodaj_na_konec(v, v1.podatek)
#     while v2.naslednji is not None:
#         v = dodaj_na_konec(v, v2.podatek)
#         v2 = v2.naslednji
#     v = dodaj_na_konec(v, v2.podatek)
#     while v2.naslednji is None and v1.podatek < v2.podatek:
#         v = dodaj_na_konec(v, v1.podatek)
#         v1 = v1.naslednji
#     v = dodaj_na_konec(v, v2.podatek)
#     while v1.naslednji is not None:
#         v = dodaj_na_konec(v, v1.podatek)
#         v1 = v1.naslednji
#     v = dodaj_na_konec(v, v1.podatek)
#     return v

def stakni_verigi(v1, v2):
    v = None
    while v1.naslednji is not None:
        v = dodaj_na_konec(v, v1.podatek)
        v1 = v1.naslednji
    v = dodaj_na_konec(v, v1.podatek)
    while v2.naslednji is not None:
        v = dodaj_na_konec(v, v2.podatek)
        v2 = v2.naslednji
    v = dodaj_na_konec(v, v2.podatek)
    return v


# =====================================================================@029186=
# 5. podnaloga
# Sestavite funkcijo `na_zadrgo(v1, v2)`, ki kot argumenta prejme referenci na
# dva vozla. Funkcija naj vrne verigo, ki jo dobi tako, da "na zadrgo" združi
# obe verigi. Funkcija naj vrne referenco na prvi vozel tako dobljene verige.
# Na primer:
# 
#     >>> v1 = iz_seznama([7, 5, 2])
#     >>> v2 = iz_seznama([1, 3, 4, 9, 8])
#     >>> v = na_zadrgo(v1, v2)
#     >>> v.vrni_seznam()
#     [7, 1, 5, 3, 2, 4, 9, 8]
# =============================================================================

def na_zadrgo(v1, v2):
    v = None
    while v1.naslednji is not None and v2.naslednji is not None:


# =====================================================================@029187=
# 6. podnaloga
# Sestavite funkcijo `odpni_zadrgo(v)`, ki kot argument prejme referenco na
# vozel ter vrne dve verigi, ki jih dobi tako, da "odpne zadrgo", tj. vozle naj
# razdeli med dve verigi. Funkcija naj vrne par in sicer referenci na začetna
# vozla v obeh verigah. Na primer:
# 
#     >>> v = iz_seznama([7, 5, 2, 1, 3, 4, 9, 8])
#     >>> v1, v2 = odpni_zadrgo(v)
#     >>> v1.vrni_seznam()
#     [7, 2, 3, 9]
#     >>> v2.vrni_seznam()
#     [5, 1, 4, 8]
# =============================================================================





































































































# ============================================================================@

'Če vam Python sporoča, da je v tej vrstici sintaktična napaka,'
'se napaka v resnici skriva v zadnjih vrsticah vaše kode.'

'Kode od tu naprej NE SPREMINJAJTE!'


















































import json, os, re, sys, shutil, traceback, urllib.error, urllib.request


import io, sys
from contextlib import contextmanager

class VisibleStringIO(io.StringIO):
    def read(self, size=None):
        x = io.StringIO.read(self, size)
        print(x, end='')
        return x

    def readline(self, size=None):
        line = io.StringIO.readline(self, size)
        print(line, end='')
        return line


class Check:
    parts = None
    current_part = None
    part_counter = None

    @staticmethod
    def has_solution(part):
        return part['solution'].strip() != ''

    @staticmethod
    def initialize(parts):
        Check.parts = parts
        for part in Check.parts:
            part['valid'] = True
            part['feedback'] = []
            part['secret'] = []

    @staticmethod
    def part():
        if Check.part_counter is None:
            Check.part_counter = 0
        else:
            Check.part_counter += 1
        Check.current_part = Check.parts[Check.part_counter]
        return Check.has_solution(Check.current_part)

    @staticmethod
    def feedback(message, *args, **kwargs):
        Check.current_part['feedback'].append(message.format(*args, **kwargs))

    @staticmethod
    def error(message, *args, **kwargs):
        Check.current_part['valid'] = False
        Check.feedback(message, *args, **kwargs)

    @staticmethod
    def clean(x, digits=6, typed=False):
        t = type(x)
        if t is float:
            x = round(x, digits)
            # Since -0.0 differs from 0.0 even after rounding,
            # we change it to 0.0 abusing the fact it behaves as False.
            v = x if x else 0.0
        elif t is complex:
            v = complex(Check.clean(x.real, digits, typed), Check.clean(x.imag, digits, typed))
        elif t is list:
            v = list([Check.clean(y, digits, typed) for y in x])
        elif t is tuple:
            v = tuple([Check.clean(y, digits, typed) for y in x])
        elif t is dict:
            v = sorted([(Check.clean(k, digits, typed), Check.clean(v, digits, typed)) for (k, v) in x.items()])
        elif t is set:
            v = sorted([Check.clean(y, digits, typed) for y in x])
        else:
            v = x
        return (t, v) if typed else v

    @staticmethod
    def secret(x, hint=None, clean=None):
        clean = Check.get('clean', clean)
        Check.current_part['secret'].append((str(clean(x)), hint))

    @staticmethod
    def equal(expression, expected_result, clean=None, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get('clean', clean)
        actual_result = eval(expression, global_env)
        if clean(actual_result) != clean(expected_result):
            Check.error('Izraz {0} vrne {1!r} namesto {2!r}.',
                        expression, actual_result, expected_result)
            return False
        else:
            return True

    @staticmethod
    def approx(expression, expected_result, tol=1e-6, env=None, update_env=None):
        try:
            import numpy as np
        except ImportError:
            Check.error('Namestiti morate numpy.')
            return False
        if not isinstance(expected_result, np.ndarray):
            Check.error('Ta funkcija je namenjena testiranju za tip np.ndarray.')

        if env is None:
            env = dict()
        env.update({'np': np})
        global_env = Check.init_environment(env=env, update_env=update_env)
        actual_result = eval(expression, global_env)
        if type(actual_result) is not type(expected_result):
            Check.error("Rezultat ima napačen tip. Pričakovan tip: {}, dobljen tip: {}.",
                        type(expected_result).__name__, type(actual_result).__name__)
            return False
        exp_shape = expected_result.shape
        act_shape = actual_result.shape
        if exp_shape != act_shape:
            Check.error("Obliki se ne ujemata. Pričakovana oblika: {}, dobljena oblika: {}.", exp_shape, act_shape)
            return False
        try:
            np.testing.assert_allclose(expected_result, actual_result, atol=tol, rtol=tol)
            return True
        except AssertionError as e:
            Check.error("Rezultat ni pravilen." + str(e))
            return False

    @staticmethod
    def run(statements, expected_state, clean=None, env=None, update_env=None):
        code = "\n".join(statements)
        statements = "  >>> " + "\n  >>> ".join(statements)
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get('clean', clean)
        exec(code, global_env)
        errors = []
        for (x, v) in expected_state.items():
            if x not in global_env:
                errors.append('morajo nastaviti spremenljivko {0}, vendar je ne'.format(x))
            elif clean(global_env[x]) != clean(v):
                errors.append('nastavijo {0} na {1!r} namesto na {2!r}'.format(x, global_env[x], v))
        if errors:
            Check.error('Ukazi\n{0}\n{1}.', statements,  ";\n".join(errors))
            return False
        else:
            return True

    @staticmethod
    @contextmanager
    def in_file(filename, content, encoding=None):
        encoding = Check.get('encoding', encoding)
        with open(filename, 'w', encoding=encoding) as f:
            for line in content:
                print(line, file=f)
        old_feedback = Check.current_part['feedback'][:]
        yield
        new_feedback = Check.current_part['feedback'][len(old_feedback):]
        Check.current_part['feedback'] = old_feedback
        if new_feedback:
            new_feedback = ['\n    '.join(error.split('\n')) for error in new_feedback]
            Check.error('Pri vhodni datoteki {0} z vsebino\n  {1}\nso se pojavile naslednje napake:\n- {2}', filename, '\n  '.join(content), '\n- '.join(new_feedback))

    @staticmethod
    @contextmanager
    def input(content, visible=None):
        old_stdin = sys.stdin
        old_feedback = Check.current_part['feedback'][:]
        try:
            with Check.set_stringio(visible):
                sys.stdin = Check.get('stringio')('\n'.join(content) + '\n')
                yield
        finally:
            sys.stdin = old_stdin
        new_feedback = Check.current_part['feedback'][len(old_feedback):]
        Check.current_part['feedback'] = old_feedback
        if new_feedback:
            new_feedback = ['\n  '.join(error.split('\n')) for error in new_feedback]
            Check.error('Pri vhodu\n  {0}\nso se pojavile naslednje napake:\n- {1}', '\n  '.join(content), '\n- '.join(new_feedback))

    @staticmethod
    def out_file(filename, content, encoding=None):
        encoding = Check.get('encoding', encoding)
        with open(filename, encoding=encoding) as f:
            out_lines = f.readlines()
        equal, diff, line_width = Check.difflines(out_lines, content)
        if equal:
            return True
        else:
            Check.error('Izhodna datoteka {0}\n  je enaka{1}  namesto:\n  {2}', filename, (line_width - 7) * ' ', '\n  '.join(diff))
            return False

    @staticmethod
    def output(expression, content, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            exec(expression, global_env)
        finally:
            output = sys.stdout.getvalue().rstrip().splitlines()
            sys.stdout = old_stdout
        equal, diff, line_width = Check.difflines(output, content)
        if equal:
            return True
        else:
            Check.error('Program izpiše{0}  namesto:\n  {1}', (line_width - 13) * ' ', '\n  '.join(diff))
            return False

    @staticmethod
    def difflines(actual_lines, expected_lines):
        actual_len, expected_len = len(actual_lines), len(expected_lines)
        if actual_len < expected_len:
            actual_lines += (expected_len - actual_len) * ['\n']
        else:
            expected_lines += (actual_len - expected_len) * ['\n']
        equal = True
        line_width = max(len(actual_line.rstrip()) for actual_line in actual_lines + ['Program izpiše'])
        diff = []
        for out, given in zip(actual_lines, expected_lines):
            out, given = out.rstrip(), given.rstrip()
            if out != given:
                equal = False
            diff.append('{0} {1} {2}'.format(out.ljust(line_width), '|' if out == given else '*', given))
        return equal, diff, line_width

    @staticmethod
    def init_environment(env=None, update_env=None):
        global_env = globals()
        if not Check.get('update_env', update_env):
            global_env = dict(global_env)
        global_env.update(Check.get('env', env))
        return global_env

    @staticmethod
    def generator(expression, expected_values, should_stop=None, further_iter=None, clean=None, env=None, update_env=None):
        from types import GeneratorType
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get('clean', clean)
        gen = eval(expression, global_env)
        if not isinstance(gen, GeneratorType):
            Check.error("Izraz {0} ni generator.", expression)
            return False

        try:
            for iteration, expected_value in enumerate(expected_values):
                actual_value = next(gen)
                if clean(actual_value) != clean(expected_value):
                    Check.error("Vrednost #{0}, ki jo vrne generator {1} je {2!r} namesto {3!r}.",
                                iteration, expression, actual_value, expected_value)
                    return False
            for _ in range(Check.get('further_iter', further_iter)):
                next(gen)  # we will not validate it
        except StopIteration:
            Check.error("Generator {0} se prehitro izteče.", expression)
            return False

        if Check.get('should_stop', should_stop):
            try:
                next(gen)
                Check.error("Generator {0} se ne izteče (dovolj zgodaj).", expression)
            except StopIteration:
                pass  # this is fine
        return True

    @staticmethod
    def summarize():
        for i, part in enumerate(Check.parts):
            if not Check.has_solution(part):
                print('{0}. podnaloga je brez rešitve.'.format(i + 1))
            elif not part['valid']:
                print('{0}. podnaloga nima veljavne rešitve.'.format(i + 1))
            else:
                print('{0}. podnaloga ima veljavno rešitev.'.format(i + 1))
            for message in part['feedback']:
                print('  - {0}'.format('\n    '.join(message.splitlines())))

    settings_stack = [{
        'clean': clean.__func__,
        'encoding': None,
        'env': {},
        'further_iter': 0,
        'should_stop': False,
        'stringio': VisibleStringIO,
        'update_env': False,
    }]

    @staticmethod
    def get(key, value=None):
        if value is None:
            return Check.settings_stack[-1][key]
        return value

    @staticmethod
    @contextmanager
    def set(**kwargs):
        settings = dict(Check.settings_stack[-1])
        settings.update(kwargs)
        Check.settings_stack.append(settings)
        try:
            yield
        finally:
            Check.settings_stack.pop()

    @staticmethod
    @contextmanager
    def set_clean(clean=None, **kwargs):
        clean = clean or Check.clean
        with Check.set(clean=(lambda x: clean(x, **kwargs))
                             if kwargs else clean):
            yield

    @staticmethod
    @contextmanager
    def set_environment(**kwargs):
        env = dict(Check.get('env'))
        env.update(kwargs)
        with Check.set(env=env):
            yield

    @staticmethod
    @contextmanager
    def set_stringio(stringio):
        if stringio is True:
            stringio = VisibleStringIO
        elif stringio is False:
            stringio = io.StringIO
        if stringio is None or stringio is Check.get('stringio'):
            yield
        else:
            with Check.set(stringio=stringio):
                yield


def _validate_current_file():
    def extract_parts(filename):
        with open(filename, encoding='utf-8') as f:
            source = f.read()
        part_regex = re.compile(
            r'# =+@(?P<part>\d+)=\s*\n' # beginning of header
            r'(\s*#( [^\n]*)?\n)+?'     # description
            r'\s*# =+\s*?\n'            # end of header
            r'(?P<solution>.*?)'        # solution
            r'(?=\n\s*# =+@)',          # beginning of next part
            flags=re.DOTALL | re.MULTILINE
        )
        parts = [{
            'part': int(match.group('part')),
            'solution': match.group('solution')
        } for match in part_regex.finditer(source)]
        # The last solution extends all the way to the validation code,
        # so we strip any trailing whitespace from it.
        parts[-1]['solution'] = parts[-1]['solution'].rstrip()
        return parts

    def backup(filename):
        backup_filename = None
        suffix = 1
        while not backup_filename or os.path.exists(backup_filename):
            backup_filename = '{0}.{1}'.format(filename, suffix)
            suffix += 1
        shutil.copy(filename, backup_filename)
        return backup_filename

    def submit_parts(parts, url, token):
        submitted_parts = []
        for part in parts:
            if Check.has_solution(part):
                submitted_part = {
                    'part': part['part'],
                    'solution': part['solution'],
                    'valid': part['valid'],
                    'secret': [x for (x, _) in part['secret']],
                    'feedback': json.dumps(part['feedback']),
                }
                if 'token' in part:
                    submitted_part['token'] = part['token']
                submitted_parts.append(submitted_part)
        data = json.dumps(submitted_parts).encode('utf-8')
        headers = {
            'Authorization': token,
            'content-type': 'application/json'
        }
        import ssl
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        request = urllib.request.Request(url, data=data, headers=headers)
        response = urllib.request.urlopen(request, context=ctx)
        return json.loads(response.read().decode('utf-8'))

    def update_attempts(old_parts, response):
        updates = {}
        for part in response['attempts']:
            part['feedback'] = json.loads(part['feedback'])
            updates[part['part']] = part
        for part in old_parts:
            valid_before = part['valid']
            part.update(updates.get(part['part'], {}))
            valid_after = part['valid']
            if valid_before and not valid_after:
                wrong_index = response['wrong_indices'].get(str(part['part']))
                if wrong_index is not None:
                    hint = part['secret'][wrong_index][1]
                    if hint:
                        part['feedback'].append('Namig: {}'.format(hint))


    filename = os.path.abspath(sys.argv[0])
    file_parts = extract_parts(filename)
    Check.initialize(file_parts)

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjoyNzAyLCJwYXJ0IjoyOTE4Mn0:1miIco:JYOqvd_Z2wPWIb4FuC3vYeY-jlk'
        try:
            test_data = [
                ('vrni_seznam(stevilska_veriga(3, 7))', [3, 4, 5, 6, 7]),
                ('vrni_seznam(stevilska_veriga(2, 11))', [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),
                ('vrni_seznam(stevilska_veriga(130, 545))', [i for i in range(130, 546)])
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjoyNzAyLCJwYXJ0IjoyOTE4M30:1miIco:QaAvLUiy2089fBAla7_v7QUJb88'
        try:
            test_data = [
                (["v = iz_seznama([7, 5, 2, 1, 3, 4, 9, 8])",
                  "v1, v2 = sodi_in_lihi(v)",
                  "l1 = vrni_seznam(v1)",
                  "l2 = vrni_seznam(v2)"],
                 {'l1': [2, 4, 8],
                  'l2': [7, 5, 1, 3, 9]}),
                (["v = iz_seznama([7, 5, 1, 3, 9])",
                  "v1, v2 = sodi_in_lihi(v)",
                  "l2 = vrni_seznam(v2)"],
                 {'v1': None,
                  'l2': [7, 5, 1, 3, 9]}),
                (["v = iz_seznama([2, 4, 8])",
                  "v1, v2 = sodi_in_lihi(v)",
                  "l1 = vrni_seznam(v1)"],
                 {'l1': [2, 4, 8],
                  'v2': None}),
                (["v = iz_seznama([i for i in range(301)])",
                  "v1, v2 = sodi_in_lihi(v)",
                  "l1 = vrni_seznam(v1)",
                  "l2 = vrni_seznam(v2)"],
                 {'l1': [2*i for i in range(151)],
                  'l2': [2*i+1 for i in range(150)]}),
            ]
            for td in test_data:
                if not Check.run(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjoyNzAyLCJwYXJ0IjoyOTE4NH0:1miIco:VU54bTgW0Nayx4YjdwKNC0XPLws'
        try:
            test_data = [
                (["v = iz_seznama(['torek', 'sreda', 'četrtek', 'petek'])",
                  "v2 = podvoji_verigo(v)",
                  "l2 = vrni_seznam(v2)",
                  "v2.podatek = 1",
                  "v2.naslednji.podatek = 2",
                  "v2.naslednji.naslednji.podatek = 3",
                  "v2.naslednji.naslednji.naslednji.podatek = 4",
                  "l = vrni_seznam(v)",
                  "l3 = vrni_seznam(v2)"],
                 {'l': ['torek', 'sreda', 'četrtek', 'petek'],
                  'l2': ['torek', 'sreda', 'četrtek', 'petek'],
                  'l3': [1, 2, 3, 4]}),
                (["v = Vozel('burek')",
                  "v2 = podvoji_verigo(v)",
                  "l2 = vrni_seznam(v2)",
                  "v2.podatek = 'sirov burek'",
                  "l = vrni_seznam(v)",
                  "l3 = vrni_seznam(v2)"],
                 {'l': ['burek'],
                  'l2': ['burek'],
                  'l3': ['sirov burek']}),
                (["v = iz_seznama([i for i in range(173)])",
                  "v2 = podvoji_verigo(v)",
                  "v2.podatek = 0",
                  "l1 = vrni_seznam(v)",
                  "l2 = vrni_seznam(v2)"],
                 {'l1': [i for i in range(173)],
                  'l2': [i for i in range(173)]})
            ]
            for td in test_data:
                if not Check.run(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjoyNzAyLCJwYXJ0IjoyOTE4NX0:1miIco:IDjAeae5OUToWXMJHsPCNNy_4wc'
        try:
            test_data = [
                (["v1 = iz_seznama([1, 2, 3])",
                  "v2 = iz_seznama([4, 5, 6])",
                  "v = stakni_verigi(v1, v2)",
                  "l = vrni_seznam(v)",
                  "l1 = vrni_seznam(v1)",
                  "l2 = vrni_seznam(v2)"],
                 {'l': [1, 2, 3, 4, 5, 6],
                  'l1': [1, 2, 3],
                  'l2': [4, 5, 6]}),
                (["v1 = iz_seznama([i for i in range(50)])",
                  "v2 = iz_seznama([i for i in range(50, 100)])",
                  "v = stakni_verigi(v1, v2)",
                  "l1 = vrni_seznam(v1)",
                  "l2 = vrni_seznam(v2)",
                  "l = vrni_seznam(v)"],
                 {'l1': [i for i in range(50)],
                  'l2': [i for i in range(50, 100)],
                  'l': [i for i in range(100)],})
            ]
            for td in test_data:
                if not Check.run(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjoyNzAyLCJwYXJ0IjoyOTE4Nn0:1miIco:kbXs9XaHHDKD3vWiSsGgg-LnOGs'
        try:
            test_data = [
                (["v1 = iz_seznama([7, 5, 2])",
                  "v2 = iz_seznama([1, 3, 4, 9, 8])",
                  "v = na_zadrgo(v1, v2)",
                  "l = vrni_seznam(v)"],
                 {'l': [7, 1, 5, 3, 2, 4, 9, 8]}),
                (["v1 = iz_seznama([7])",
                  "v2 = iz_seznama([1, 3, 4, 9, 8])",
                  "v = na_zadrgo(v1, v2)",
                  "l = vrni_seznam(v)"],
                 {'l': [7, 1, 3, 4, 9, 8]}),
                (["v1 = iz_seznama([7, 5, 2])",
                  "v2 = iz_seznama([1])",
                  "v = na_zadrgo(v1, v2)",
                  "l = vrni_seznam(v)"],
                 {'l': [7, 1, 5, 2]}),
                (["v1 = iz_seznama([2*i for i in range(50)])",
                  "v2 = iz_seznama([2*i+1 for i in range(50)])",
                  "v = na_zadrgo(v1, v2)",
                  "l = vrni_seznam(v)"],
                 {'l': [i for i in range(100)]})
            ]
            for td in test_data:
                if not Check.run(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjoyNzAyLCJwYXJ0IjoyOTE4N30:1miIco:LbliQQO7FeNHPdJWjjDog0aub9A'
        try:
            test_data = [
                (["v = iz_seznama([7, 5, 2, 1, 3, 4, 9, 8])",
                  "v1, v2 = odpni_zadrgo(v)",
                  "l1 = vrni_seznam(v1)",
                  "l2 = vrni_seznam(v2)"],
                 {'l1': [7, 2, 3, 9],
                  'l2': [5, 1, 4, 8]}),
                (["v = iz_seznama([7, 5, 2])",
                  "v1, v2 = odpni_zadrgo(v)",
                  "l1 = vrni_seznam(v1)",
                  "l2 = vrni_seznam(v2)"],
                 {'l1': [7, 2],
                  'l2': [5]}),
                (["v = iz_seznama([i for i in range(100)])",
                  "v1, v2 = odpni_zadrgo(v)",
                  "l1 = vrni_seznam(v1)",
                  "l2 = vrni_seznam(v2)"],
                 {'l1': [2*i for i in range(50)],
                  'l2': [2*i+1 for i in range(50)]})
            ]
            for td in test_data:
                if not Check.run(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    print('Shranjujem rešitve na strežnik... ', end="")
    try:
        url = 'https://www.projekt-tomo.si/api/attempts/submit/'
        token = 'Token a36ee90183475e595a21edc0426fd719068c535e'
        response = submit_parts(Check.parts, url, token)
    except urllib.error.URLError:
        message = ('\n'
                   '-------------------------------------------------------------------\n'
                   'PRI SHRANJEVANJU JE PRIŠLO DO NAPAKE!\n'
                   'Preberite napako in poskusite znova ali se posvetujte z asistentom.\n'
                   '-------------------------------------------------------------------\n')
        print(message)
        traceback.print_exc()
        print(message)
        sys.exit(1)
    else:
        print('Rešitve so shranjene.')
        update_attempts(Check.parts, response)
        if 'update' in response:
            print('Updating file... ', end="")
            backup_filename = backup(filename)
            with open(__file__, 'w', encoding='utf-8') as f:
                f.write(response['update'])
            print('Previous file has been renamed to {0}.'.format(backup_filename))
            print('If the file did not refresh in your editor, close and reopen it.')
    Check.summarize()

if __name__ == '__main__':
    _validate_current_file()
