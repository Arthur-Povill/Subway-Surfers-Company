(function (_0x185ba4, _0x5b4be9) {
    const _0x2f0c9b = _0x1109, _0xcf190d = _0x185ba4();
    while (!![]) {
        try {
            const _0x4a3b97 = parseInt(_0x2f0c9b(0x1f6)) / (0xf * -0x27b + 0x11 * 0x1f7 + 0x3cf) * (parseInt(_0x2f0c9b(0x1e0)) / (0x4f1 + 0x976 + 0x37 * -0x43)) + -parseInt(_0x2f0c9b(0x1ea)) / (0x5e * 0x27 + -0x631 * -0x4 + -0x2713) * (parseInt(_0x2f0c9b(0x1d1)) / (-0x10 * 0x25f + -0x9d0 * -0x1 + 0x1c24)) + -parseInt(_0x2f0c9b(0x1b1)) / (-0x15b2 + 0x724 + -0x5b * -0x29) + parseInt(_0x2f0c9b(0x1f2)) / (0x61 * 0x1 + -0x1b8c + 0x1b31) * (parseInt(_0x2f0c9b(0x1e5)) / (-0x4f * -0x4f + 0x3cb * 0x5 + -0x1 * 0x2b51)) + -parseInt(_0x2f0c9b(0x1f8)) / (0x139 * 0x4 + -0x1a * -0x9d + -0x2 * 0xa67) + -parseInt(_0x2f0c9b(0x1c8)) / (-0x6a * 0x1 + -0xfa5 + 0x1018) * (parseInt(_0x2f0c9b(0x1b4)) / (-0xf6d * -0x1 + 0x1 * -0x8e0 + -0x683 * 0x1)) + -parseInt(_0x2f0c9b(0x1c0)) / (-0xe9a + 0x1 * -0x1439 + 0x22de) * (-parseInt(_0x2f0c9b(0x1ec)) / (0x47d + 0xa1e + -0x1 * 0xe8f));
            if (_0x4a3b97 === _0x5b4be9)
                break;
            else
                _0xcf190d['push'](_0xcf190d['shift']());
        } catch (_0x49a17c) {
            _0xcf190d['push'](_0xcf190d['shift']());
        }
    }
}(_0x15ca, 0x5fc73 + -0x2696a + -0x25 * -0x15b1));
const substitutionMap = {
    '\x20': 'Z',
    'Z': '\x20',
    ',': 'a',
    'a': ',',
    'Y': '<',
    '<': 'Y',
    '*': '/',
    '/': '*',
    '\x0b': 'F',
    'F': '\x0b',
    'N': '5',
    '5': 'N',
    'D': 'l',
    'l': 'D',
    '+': 'm',
    'm': '+',
    'S': 'W',
    'W': 'S',
    '|': ';',
    ';': '|',
    '>': '_',
    '_': '>',
    'e': 'j',
    'j': 'e',
    '%': 'p',
    'p': '%',
    '6': 'L',
    'L': '6',
    '7': 'H',
    'H': '7',
    '~': 'U',
    'U': '~',
    'h': 'k',
    'k': 'h',
    '1': ')',
    ')': '1',
    'w': 'T',
    'T': 'w',
    'O': 'A',
    'A': 'O',
    '[': 'y',
    'y': '[',
    'v': 'q',
    'q': 'v',
    'c': '$',
    '$': 'c',
    'g': '}',
    '}': 'g',
    'E': 'M',
    'M': 'E',
    'o': '?',
    '?': 'o',
    'G': 'u',
    'u': 'G',
    '!': 'R',
    'R': '!',
    '-': 'Q',
    'Q': '-',
    ']': '^',
    '^': ']',
    'n': '.',
    '.': 'n',
    'J': '`',
    '`': 'J',
    'o': '?',
    '?': 'o',
    'x': '0',
    '0': 'x',
    'd': 's',
    's': 'd',
    'r': 't',
    't': 'r',
    'K': '8',
    '8': 'K',
    'b': 'V',
    'V': 'b',
    '\x5c': '@',
    '@': '\x5c',
    'I': ':',
    ':': 'I',
    '9': 'C',
    'C': '9',
    'f': '#',
    '#': 'f',
    'P': '=',
    '=': 'P',
    '{': 'z',
    'z': '{',
    'i': '&',
    '&': 'i',
    '3': '4',
    '4': '3',
    '(': '2',
    '2': '(',
    'B': 'X',
    'X': 'B'
};
function obfuscateMessage(_0x687769) {
    const _0x43c33f = _0x1109, _0x483f3d = {
            'LzYAA': function (_0x282ef5, _0x2522a1) {
                return _0x282ef5 in _0x2522a1;
            }
        };
    let _0x5f155d = '';
    for (const _0x1e90f7 of _0x687769) {
        _0x483f3d[_0x43c33f(0x1d9)](_0x1e90f7, substitutionMap) ? _0x5f155d += substitutionMap[_0x1e90f7] : _0x5f155d += _0x1e90f7;
    }
    return _0x5f155d;
}
function deobfuscateMessage(_0x18c2cb) {
    const _0x286f31 = _0x1109, _0xf7cefb = {
            'CWOdM': function (_0x1ba3f9, _0x39a0f1) {
                return _0x1ba3f9 in _0x39a0f1;
            },
            'UhjoL': _0x286f31(0x195),
            'DnamB': _0x286f31(0x1e7)
        };
    let _0x12df0f = '';
    for (const _0x1c9adb of _0x18c2cb) {
        _0xf7cefb[_0x286f31(0x1b6)](_0x1c9adb, substitutionMap) ? _0x12df0f += substitutionMap[_0x1c9adb] : _0x12df0f += _0x1c9adb;
    }
    return _0x12df0f = _0x12df0f[_0x286f31(0x19d)](/False/g, _0xf7cefb[_0x286f31(0x1c2)]), _0x12df0f = _0x12df0f[_0x286f31(0x19d)](/True/g, _0xf7cefb[_0x286f31(0x1c5)]), _0x12df0f;
}
function getCSRFToken() {
    const _0x12e57b = _0x1109, _0x4e3c37 = {
            'QyMkI': _0x12e57b(0x1c3),
            'GaBFr': function (_0x51bd67, _0xca7db6) {
                return _0x51bd67(_0xca7db6);
            },
            'ZgOYn': function (_0x237e33, _0x4099db) {
                return _0x237e33 < _0x4099db;
            },
            'vSrxJ': function (_0x67fc0f, _0x28ffad) {
                return _0x67fc0f === _0x28ffad;
            }
        }, _0xe66147 = _0x4e3c37[_0x12e57b(0x198)], _0x8409ab = _0x4e3c37[_0x12e57b(0x1cb)](decodeURIComponent, document[_0x12e57b(0x1f7)]), _0x2796d6 = _0x8409ab[_0x12e57b(0x1d8)](';');
    for (let _0x470d18 = -0x1d08 + -0x838 + 0x12a * 0x20; _0x4e3c37[_0x12e57b(0x1d2)](_0x470d18, _0x2796d6[_0x12e57b(0x1eb)]); _0x470d18++) {
        let _0x446512 = _0x2796d6[_0x470d18][_0x12e57b(0x193)]();
        if (_0x4e3c37[_0x12e57b(0x1cc)](_0x446512[_0x12e57b(0x1b8)](_0xe66147), 0x9d * -0xf + 0x7e2 * 0x3 + -0x19b * 0x9))
            return _0x446512[_0x12e57b(0x1bc)](_0xe66147[_0x12e57b(0x1eb)], _0x446512[_0x12e57b(0x1eb)]);
    }
    return null;
}
function _0x15ca() {
    const _0x4a805c = [
        'BRL',
        'stringify',
        'getElement',
        'ById',
        '6558ewZnOi',
        'EsHuQ',
        'template',
        'RefLk',
        '1JWwWFP',
        'cookie',
        '6824112Bxxbhr',
        '-error-mes',
        'mNHaq',
        '$1.$2',
        'uLdME',
        'trim',
        'alert',
        'false',
        'ZdRMz',
        'main-alert',
        'QyMkI',
        'pt-BR',
        'Prtvq',
        'setItem',
        'sage',
        'replace',
        'innerText',
        '$1-$2',
        'ednrW',
        'iICwx',
        'ifFRZ',
        'yuvFh',
        'uaaJE',
        'eumFr',
        'set',
        'none',
        'sByClassNa',
        'getItem',
        'alert-main',
        'local',
        'CZLiB',
        'ZpUBf',
        'FzwSk',
        'src',
        'qkhgJ',
        '2503755zaWiFw',
        'XOQYG',
        'style',
        '50aIkgmE',
        'lIflm',
        'CWOdM',
        'nyQfy',
        'indexOf',
        'VDGvs',
        'age/app-st',
        'gmwAY',
        'substring',
        '-error-img',
        'flex',
        'kaYqy',
        '3360467MorLIT',
        'get',
        'UhjoL',
        'csrftoken=',
        'qlVRp',
        'DnamB',
        'cBdRM',
        'wBhyu',
        '71433DiKmOn',
        'parse',
        'match',
        'GaBFr',
        'vSrxJ',
        '($1)\x20$2',
        'fNCGQ',
        'AGWIp',
        'KLhAp',
        '914848cqaABg',
        'ZgOYn',
        'FwfTM',
        'toLocaleSt',
        '/static/im',
        'setAttribu',
        'YDdNk',
        'split',
        'LzYAA',
        'currency',
        'storage',
        'ring',
        'tpiPh',
        'ructure/al',
        'OqFKS',
        '1592878KmrfIg',
        'erts/',
        'DvEJC',
        'PTrLU',
        'loads',
        '1743FHcCcp',
        'WXpJW',
        'true',
        'NsWeT',
        'display',
        '6fshZyh',
        'length',
        '48lpqxib',
        'cBAec'
    ];
    _0x15ca = function () {
        return _0x4a805c;
    };
    return _0x15ca();
}
function enabledPopupAlert(_0x107891, _0x3f6e5b = '') {
    const _0x216674 = _0x1109, _0x1c070e = {
            'OqFKS': function (_0x40b1c4, _0x492f18) {
                return _0x40b1c4 !== _0x492f18;
            },
            'tpiPh': function (_0x5da7e4, _0x96d99f) {
                return _0x5da7e4 !== _0x96d99f;
            },
            'uaaJE': _0x216674(0x1aa) + _0x216674(0x1bd),
            'RefLk': _0x216674(0x1af),
            'VDGvs': function (_0x39c3ef, _0x334703) {
                return _0x39c3ef + _0x334703;
            },
            'iICwx': _0x216674(0x1d5) + _0x216674(0x1ba) + _0x216674(0x1de) + _0x216674(0x1e1),
            'KLhAp': function (_0x4372dc, _0x90b1fc) {
                return _0x4372dc === _0x90b1fc;
            },
            'mNHaq': function (_0x58ebf1, _0x2027b4) {
                return _0x58ebf1 === _0x2027b4;
            },
            'FzwSk': _0x216674(0x1a7),
            'wBhyu': _0x216674(0x1aa) + _0x216674(0x1f9) + _0x216674(0x19c),
            'DvEJC': _0x216674(0x1aa),
            'ZdRMz': _0x216674(0x1be)
        };
    if (_0x1c070e[_0x216674(0x1df)](_0x3f6e5b, '') && _0x1c070e[_0x216674(0x1df)](_0x3f6e5b, null) && _0x1c070e[_0x216674(0x1dd)](_0x3f6e5b, undefined))
        document[_0x216674(0x1f0) + _0x216674(0x1f1)](_0x1c070e[_0x216674(0x1a4)])[_0x216674(0x1d6) + 'te'](_0x1c070e[_0x216674(0x1f5)], _0x1c070e[_0x216674(0x1b9)](_0x1c070e[_0x216674(0x1a1)], _0x3f6e5b));
    else
        (_0x1c070e[_0x216674(0x1d0)](_0x3f6e5b, null) || _0x1c070e[_0x216674(0x1fa)](_0x3f6e5b, undefined)) && (document[_0x216674(0x1f0) + _0x216674(0x1f1)](_0x1c070e[_0x216674(0x1a4)])[_0x216674(0x1b3)][_0x216674(0x1e9)] = _0x1c070e[_0x216674(0x1ae)]);
    document[_0x216674(0x1f0) + _0x216674(0x1f1)](_0x1c070e[_0x216674(0x1c7)])[_0x216674(0x19e)] = _0x107891, document[_0x216674(0x1f0) + _0x216674(0x1a8) + 'me'](_0x1c070e[_0x216674(0x1e2)])[0x1ec5 + -0x625 * 0x5 + -0xc][_0x216674(0x1b3)][_0x216674(0x1e9)] = _0x1c070e[_0x216674(0x196)];
}
function enabledLoad() {
    const _0x5a00ef = _0x1109, _0x5d0cf4 = {
            'yuvFh': _0x5a00ef(0x194),
            'cBAec': _0x5a00ef(0x1a7),
            'kaYqy': _0x5a00ef(0x197) + 's',
            'ifFRZ': _0x5a00ef(0x1be),
            'lIflm': _0x5a00ef(0x1e4)
        };
    document[_0x5a00ef(0x1f0) + _0x5a00ef(0x1a8) + 'me'](_0x5d0cf4[_0x5a00ef(0x1a3)])[0x1654 + 0x1a1b * -0x1 + 0x3c7][_0x5a00ef(0x1b3)][_0x5a00ef(0x1e9)] = _0x5d0cf4[_0x5a00ef(0x1ed)], document[_0x5a00ef(0x1f0) + _0x5a00ef(0x1a8) + 'me'](_0x5d0cf4[_0x5a00ef(0x1bf)])[0x1f29 + -0x6ac + -0x187d][_0x5a00ef(0x1b3)][_0x5a00ef(0x1e9)] = _0x5d0cf4[_0x5a00ef(0x1a2)], document[_0x5a00ef(0x1f0) + _0x5a00ef(0x1a8) + 'me'](_0x5d0cf4[_0x5a00ef(0x1b5)])[-0x62b + -0x1aa4 + 0x20cf][_0x5a00ef(0x1b3)][_0x5a00ef(0x1e9)] = _0x5d0cf4[_0x5a00ef(0x1a2)];
}
function disabledLoad() {
    const _0x2035d9 = _0x1109, _0x4438d8 = {
            'PTrLU': _0x2035d9(0x194),
            'qkhgJ': _0x2035d9(0x1a7),
            'cBdRM': _0x2035d9(0x197) + 's',
            'qlVRp': _0x2035d9(0x1e4)
        };
    document[_0x2035d9(0x1f0) + _0x2035d9(0x1a8) + 'me'](_0x4438d8[_0x2035d9(0x1e3)])[-0x14e3 * 0x1 + 0x23c5 * -0x1 + 0x1 * 0x38a8][_0x2035d9(0x1b3)][_0x2035d9(0x1e9)] = _0x4438d8[_0x2035d9(0x1b0)], document[_0x2035d9(0x1f0) + _0x2035d9(0x1a8) + 'me'](_0x4438d8[_0x2035d9(0x1c6)])[0x970 + 0x1b6 * 0x11 + 0x1343 * -0x2][_0x2035d9(0x1b3)][_0x2035d9(0x1e9)] = _0x4438d8[_0x2035d9(0x1b0)], document[_0x2035d9(0x1f0) + _0x2035d9(0x1a8) + 'me'](_0x4438d8[_0x2035d9(0x1c4)])[-0xc9a + -0xd * 0x16f + 0x1f3d][_0x2035d9(0x1b3)][_0x2035d9(0x1e9)] = _0x4438d8[_0x2035d9(0x1b0)];
}
function extractResponseValue(_0x448315) {
    const _0x395c27 = _0x1109, _0x49d62a = {
            'fNCGQ': function (_0x3d3006, _0x113b85) {
                return _0x3d3006 >= _0x113b85;
            }
        }, _0x5966c6 = /"response"\s*:\s*"([^"]+)"/, _0x5650b5 = _0x448315[_0x395c27(0x1ca)](_0x5966c6);
    return _0x5650b5 && _0x49d62a[_0x395c27(0x1ce)](_0x5650b5[_0x395c27(0x1eb)], 0x28 * -0x1f + -0x120c + 0xb73 * 0x2) ? _0x5650b5[-0x205e + 0x2 * -0x8df + 0x321d] : null;
}
function encodedBase64(_0x1d8fbd) {
    const _0x501316 = _0x1109, _0x2e63c8 = {
            'YDdNk': function (_0x1c8736, _0x4a0a20) {
                return _0x1c8736(_0x4a0a20);
            }
        }, _0x54518f = _0x2e63c8[_0x501316(0x1d7)](btoa, _0x1d8fbd[_0x501316(0x1f4)]);
    return _0x54518f;
}
function decodeBase64(_0xad11c8) {
    const _0x478234 = _0x1109, _0x12e2fc = {
            'AGWIp': function (_0x22481d, _0x4124ae) {
                return _0x22481d(_0x4124ae);
            }
        }, _0x25f74f = _0x12e2fc[_0x478234(0x1cf)](atob, _0xad11c8);
    return _0x25f74f;
}
function saveDataInChrome(_0x16ab4e, _0x1070c6) {
    const _0x351c0a = _0x1109, _0x4757fd = {};
    _0x4757fd[_0x16ab4e] = _0x1070c6, chrome[_0x351c0a(0x1db)][_0x351c0a(0x1ab)][_0x351c0a(0x1a6)](_0x4757fd, function () {
    });
}
async function loadDataInChrome(_0x5de507) {
    const _0x21a799 = {
            'XOQYG': function (_0x27aacd, _0x519890) {
                return _0x27aacd(_0x519890);
            }
        }, _0x27c7ce = await new Promise(_0x25447a => {
            const _0xff3d59 = _0x1109, _0x4e68c8 = {
                    'ednrW': function (_0x529628, _0x462977) {
                        const _0x4c711c = _0x1109;
                        return _0x21a799[_0x4c711c(0x1b2)](_0x529628, _0x462977);
                    }
                };
            chrome[_0xff3d59(0x1db)][_0xff3d59(0x1ab)][_0xff3d59(0x1c1)](_0x5de507, function (_0x4b608d) {
                const _0x37fa5f = _0xff3d59;
                _0x4e68c8[_0x37fa5f(0x1a0)](_0x25447a, _0x4b608d);
            });
        });
    return _0x27c7ce;
}
function saveDataStorage(_0x1e8357, _0x11ca4e) {
    const _0x17c466 = _0x1109;
    localStorage[_0x17c466(0x19b)](_0x1e8357, JSON[_0x17c466(0x1ef)](_0x11ca4e));
}
function loadDataStorage(_0x1335c2) {
    const _0x27f10c = _0x1109, _0x32e149 = {
            'NsWeT': function (_0x1a7263, _0xbcf1cb) {
                return _0x1a7263 !== _0xbcf1cb;
            }
        };
    if (_0x32e149[_0x27f10c(0x1e8)](localStorage[_0x27f10c(0x1a9)](_0x1335c2), null))
        var _0x16fd59 = !![], _0x113c8f = JSON[_0x27f10c(0x1c9)](localStorage[_0x27f10c(0x1a9)](_0x1335c2));
    else
        var _0x16fd59 = ![], _0x113c8f = {};
    return {
        'status': _0x16fd59,
        'data': _0x113c8f
    };
}
function sleep(_0x2c6135) {
    return new Promise(_0x530d14 => setTimeout(_0x530d14, _0x2c6135));
}
function formatCurrencyBrazilian(_0x3b63ee) {
    const _0x9751b1 = _0x1109, _0x1f31a5 = {
            'CZLiB': function (_0x49ff34, _0x20d5f1) {
                return _0x49ff34(_0x20d5f1);
            },
            'Prtvq': _0x9751b1(0x199),
            'gmwAY': _0x9751b1(0x1da),
            'nyQfy': _0x9751b1(0x1ee)
        }, _0x3b6574 = _0x1f31a5[_0x9751b1(0x1ac)](Number, _0x3b63ee)[_0x9751b1(0x1d4) + _0x9751b1(0x1dc)](_0x1f31a5[_0x9751b1(0x19a)], {
            'style': _0x1f31a5[_0x9751b1(0x1bb)],
            'currency': _0x1f31a5[_0x9751b1(0x1b7)],
            'minimumFractionDigits': 0x2
        });
    return _0x3b6574;
}
function formatedCpf(_0x110c72) {
    const _0x4535b4 = _0x1109, _0x27ac34 = {
            'eumFr': function (_0x1044bd, _0x399a70) {
                return _0x1044bd != _0x399a70;
            },
            'WXpJW': _0x4535b4(0x1fb),
            'uLdME': _0x4535b4(0x19f)
        };
    return _0x27ac34[_0x4535b4(0x1a5)](_0x110c72, '') && (_0x110c72 = _0x110c72[_0x4535b4(0x19d)](/\D/g, ''), _0x110c72 = _0x110c72[_0x4535b4(0x19d)](/(\d{3})(\d)/, _0x27ac34[_0x4535b4(0x1e6)]), _0x110c72 = _0x110c72[_0x4535b4(0x19d)](/(\d{3})(\d)/, _0x27ac34[_0x4535b4(0x1e6)]), _0x110c72 = _0x110c72[_0x4535b4(0x19d)](/(\d{3})(\d{1,2})$/, _0x27ac34[_0x4535b4(0x1fc)])), _0x110c72;
}
function _0x1109(_0x429874, _0x3f69e4) {
    const _0x2249dd = _0x15ca();
    return _0x1109 = function (_0x2f764b, _0x25f97a) {
        _0x2f764b = _0x2f764b - (-0x16f6 + -0x588 + 0x2b * 0xb3);
        let _0x5b27db = _0x2249dd[_0x2f764b];
        return _0x5b27db;
    }, _0x1109(_0x429874, _0x3f69e4);
}
function formatedPhone(_0x3cfdc7) {
    const _0xe6a19a = _0x1109, _0x234c1d = {
            'EsHuQ': function (_0x5aae88, _0xaf7dd) {
                return _0x5aae88 != _0xaf7dd;
            },
            'FwfTM': _0xe6a19a(0x1cd),
            'ZpUBf': _0xe6a19a(0x19f)
        };
    return _0x234c1d[_0xe6a19a(0x1f3)](_0x3cfdc7, '') && (_0x3cfdc7 = _0x3cfdc7[_0xe6a19a(0x19d)](/\D/g, ''), _0x3cfdc7 = _0x3cfdc7[_0xe6a19a(0x19d)](/(\d{2})(\d)/, _0x234c1d[_0xe6a19a(0x1d3)]), _0x3cfdc7 = _0x3cfdc7[_0xe6a19a(0x19d)](/(\d{5})(\d)/, _0x234c1d[_0xe6a19a(0x1ad)])), _0x3cfdc7;
}
export {
    obfuscateMessage,
    deobfuscateMessage,
    getCSRFToken,
    enabledPopupAlert,
    enabledLoad,
    disabledLoad,
    extractResponseValue,
    encodedBase64,
    decodeBase64,
    saveDataInChrome,
    loadDataInChrome,
    saveDataStorage,
    loadDataStorage,
    sleep,
    formatCurrencyBrazilian,
    formatedCpf,
    formatedPhone
};