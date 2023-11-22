(function (_0x1ee2d8, _0x26ece5) {
    const _0x5494e8 = _0x113d, _0x5b9fc6 = _0x1ee2d8();
    while (!![]) {
        try {
            const _0x3bcf50 = parseInt(_0x5494e8(0x15e)) / (0x2223 + -0x228f + 0x1 * 0x6d) + parseInt(_0x5494e8(0x171)) / (-0x1 * -0x22f9 + 0x21 * 0xc1 + -0x3bd8) + parseInt(_0x5494e8(0x13c)) / (0x5bf * 0x1 + -0x263 + 0x359 * -0x1) + -parseInt(_0x5494e8(0x178)) / (-0x5 * -0x59 + 0x1c * -0x2e + -0x7 * -0x79) + parseInt(_0x5494e8(0x1a9)) / (0x1cb5 + 0xc5 * -0x1d + -0x65f) + parseInt(_0x5494e8(0x18e)) / (0x425 + -0x1e29 + -0x21 * -0xca) * (parseInt(_0x5494e8(0x190)) / (-0x2572 + -0x22e6 + 0x485f)) + -parseInt(_0x5494e8(0x147)) / (0x4e8 + -0x1d30 + -0x30a * -0x8) * (parseInt(_0x5494e8(0x19d)) / (-0x1378 + -0xa94 + 0x1e15));
            if (_0x3bcf50 === _0x26ece5)
                break;
            else
                _0x5b9fc6['push'](_0x5b9fc6['shift']());
        } catch (_0x15cefc) {
            _0x5b9fc6['push'](_0x5b9fc6['shift']());
        }
    }
}(_0x501d, 0x32f * -0xc7 + 0x15d * 0x1eb + 0x217c3));
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
function obfuscateMessage(_0x4df308) {
    const _0x2b69c2 = _0x113d, _0x15791e = {
            'DbCWG': function (_0x553294, _0x12dbd5) {
                return _0x553294 in _0x12dbd5;
            }
        };
    let _0x4122dd = '';
    for (const _0x3b9748 of _0x4df308) {
        _0x15791e[_0x2b69c2(0x184)](_0x3b9748, substitutionMap) ? _0x4122dd += substitutionMap[_0x3b9748] : _0x4122dd += _0x3b9748;
    }
    return _0x4122dd;
}
function deobfuscateMessage(_0x460ede) {
    const _0x1baead = _0x113d, _0x4e637b = {
            'mXBjJ': function (_0x90428, _0x44f64f) {
                return _0x90428 in _0x44f64f;
            },
            'wkXRr': _0x1baead(0x164),
            'yATlg': _0x1baead(0x163)
        };
    let _0x4a195e = '';
    for (const _0x456d8b of _0x460ede) {
        _0x4e637b[_0x1baead(0x150)](_0x456d8b, substitutionMap) ? _0x4a195e += substitutionMap[_0x456d8b] : _0x4a195e += _0x456d8b;
    }
    return _0x4a195e = _0x4a195e[_0x1baead(0x182)](/False/g, _0x4e637b[_0x1baead(0x187)]), _0x4a195e = _0x4a195e[_0x1baead(0x182)](/True/g, _0x4e637b[_0x1baead(0x179)]), _0x4a195e;
}
function getCSRFToken() {
    const _0x4c2aad = _0x113d, _0x5bcb06 = {
            'LWMMk': _0x4c2aad(0x17d),
            'bTlCw': function (_0x58dc7b, _0x4c6095) {
                return _0x58dc7b(_0x4c6095);
            },
            'UXvTl': function (_0xa7a82c, _0x89e270) {
                return _0xa7a82c < _0x89e270;
            },
            'CYttI': function (_0x5c782a, _0x31c4dc) {
                return _0x5c782a === _0x31c4dc;
            }
        }, _0x5a89d7 = _0x5bcb06[_0x4c2aad(0x1a5)], _0x408000 = _0x5bcb06[_0x4c2aad(0x16e)](decodeURIComponent, document[_0x4c2aad(0x18d)]), _0x311360 = _0x408000[_0x4c2aad(0x194)](';');
    for (let _0x12be49 = 0xca7 + 0x9ed * -0x3 + -0x89 * -0x20; _0x5bcb06[_0x4c2aad(0x146)](_0x12be49, _0x311360[_0x4c2aad(0x1a7)]); _0x12be49++) {
        let _0x5925b4 = _0x311360[_0x12be49][_0x4c2aad(0x1aa)]();
        if (_0x5bcb06[_0x4c2aad(0x199)](_0x5925b4[_0x4c2aad(0x151)](_0x5a89d7), -0x22ab + -0x1ce4 + 0x35 * 0x133))
            return _0x5925b4[_0x4c2aad(0x14d)](_0x5a89d7[_0x4c2aad(0x1a7)], _0x5925b4[_0x4c2aad(0x1a7)]);
    }
    return null;
}
function enabledPopupAlert(_0x35cec8, _0x380ecb = '') {
    const _0x2218d3 = _0x113d, _0x593c67 = {
            'thlAh': function (_0x428cc5, _0x5d8005) {
                return _0x428cc5 !== _0x5d8005;
            },
            'VQkTf': function (_0x1f548c, _0x4b3928) {
                return _0x1f548c !== _0x4b3928;
            },
            'gjAYb': _0x2218d3(0x1a3) + _0x2218d3(0x1a1),
            'vSXYH': function (_0x111665, _0x4a5082) {
                return _0x111665 === _0x4a5082;
            },
            'lvaXe': _0x2218d3(0x174) + 'g',
            'oatEK': _0x2218d3(0x140) + _0x2218d3(0x198),
            'eUQAL': _0x2218d3(0x14a),
            'dgvbP': function (_0x2b45c2, _0x51270c) {
                return _0x2b45c2 + _0x51270c;
            },
            'zbjYA': _0x2218d3(0x1a2) + _0x2218d3(0x189) + _0x2218d3(0x149),
            'UJHQj': function (_0x3373d4, _0x3bc321) {
                return _0x3373d4 + _0x3bc321;
            },
            'cvVvU': _0x2218d3(0x183) + _0x2218d3(0x169) + 's/',
            'GLizt': _0x2218d3(0x19e),
            'LmRtZ': function (_0x2ef082, _0x1017c9) {
                return _0x2ef082 === _0x1017c9;
            },
            'vcXNx': _0x2218d3(0x165),
            'SJkmU': _0x2218d3(0x140) + _0x2218d3(0x19a) + _0x2218d3(0x154),
            'LqXTy': _0x2218d3(0x140),
            'WjjNA': _0x2218d3(0x196)
        };
    if (_0x593c67[_0x2218d3(0x17b)](_0x380ecb, '') && _0x593c67[_0x2218d3(0x191)](_0x380ecb, null) && _0x593c67[_0x2218d3(0x17b)](_0x380ecb, undefined)) {
        var _0x171dc2 = document[_0x2218d3(0x14f) + _0x2218d3(0x158)](_0x593c67[_0x2218d3(0x15b)])[_0x2218d3(0x15a)];
        _0x593c67[_0x2218d3(0x1ab)](_0x380ecb, _0x593c67[_0x2218d3(0x166)]) ? document[_0x2218d3(0x14f) + _0x2218d3(0x158)](_0x593c67[_0x2218d3(0x13f)])[_0x2218d3(0x157) + 'te'](_0x593c67[_0x2218d3(0x19f)], _0x593c67[_0x2218d3(0x177)](_0x593c67[_0x2218d3(0x177)](_0x171dc2, _0x593c67[_0x2218d3(0x14b)]), _0x380ecb)) : document[_0x2218d3(0x14f) + _0x2218d3(0x158)](_0x593c67[_0x2218d3(0x13f)])[_0x2218d3(0x157) + 'te'](_0x593c67[_0x2218d3(0x19f)], _0x593c67[_0x2218d3(0x15d)](_0x593c67[_0x2218d3(0x15d)](_0x171dc2, _0x593c67[_0x2218d3(0x17e)]), _0x593c67[_0x2218d3(0x141)]));
    } else
        (_0x593c67[_0x2218d3(0x1ab)](_0x380ecb, null) || _0x593c67[_0x2218d3(0x13e)](_0x380ecb, undefined)) && (document[_0x2218d3(0x14f) + _0x2218d3(0x158)](_0x593c67[_0x2218d3(0x13f)])[_0x2218d3(0x16a)][_0x2218d3(0x155)] = _0x593c67[_0x2218d3(0x1a4)]);
    document[_0x2218d3(0x14f) + _0x2218d3(0x158)](_0x593c67[_0x2218d3(0x192)])[_0x2218d3(0x19b)] = _0x35cec8, document[_0x2218d3(0x14f) + _0x2218d3(0x16d) + 'me'](_0x593c67[_0x2218d3(0x185)])[0x2 * -0xbd7 + -0xef9 + 0x26a7][_0x2218d3(0x16a)][_0x2218d3(0x155)] = _0x593c67[_0x2218d3(0x14e)];
}
function _0x501d() {
    const _0x209805 = [
        'ryTiu',
        'toLocaleSt',
        'get',
        'NJHNC',
        'UXvTl',
        '8lbxCOP',
        'loads',
        'alerts/',
        'src',
        'zbjYA',
        'parse',
        'substring',
        'WjjNA',
        'getElement',
        'mXBjJ',
        'indexOf',
        'rJvee',
        'SIPbo',
        'sage',
        'display',
        '($1)\x20$2',
        'setAttribu',
        'ById',
        '$1-$2',
        'value',
        'gjAYb',
        'set',
        'UJHQj',
        '41916WsBIrW',
        'BRL',
        'pt-BR',
        'setItem',
        'AfKKr',
        'true',
        'false',
        'none',
        'lvaXe',
        'RJXCE',
        'currency',
        'kbot/alert',
        'style',
        'rTqBX',
        'XgVQF',
        'sByClassNa',
        'bTlCw',
        'vOvnE',
        'match',
        '428708RGkooQ',
        'ZUiLR',
        'getItem',
        'correct.pn',
        'TkTTR',
        'OxEZL',
        'dgvbP',
        '191524PnEUht',
        'yATlg',
        'gqfdM',
        'thlAh',
        'fPFeu',
        'csrftoken=',
        'cvVvU',
        'EWhRf',
        'alert',
        'stringify',
        'replace',
        'image/shar',
        'DbCWG',
        'LqXTy',
        'ring',
        'wkXRr',
        'YFIwV',
        'structure/',
        'AGlFp',
        'template',
        'lIOEi',
        'cookie',
        '6408cSBoFp',
        'nIIzr',
        '931DXkFHV',
        'VQkTf',
        'SJkmU',
        'ciHyp',
        'split',
        '$1.$2',
        'flex',
        'ojtwL',
        '-error-img',
        'CYttI',
        '-error-mes',
        'innerText',
        'GwFqz',
        '4861629rhHrSC',
        'error.png',
        'eUQAL',
        'NWOyK',
        'ticFile',
        'image/app-',
        'dynamicSta',
        'vcXNx',
        'LWMMk',
        'xGUqJ',
        'length',
        'storage',
        '1200725bvCKcS',
        'trim',
        'vSXYH',
        'local',
        '287796EPSsJV',
        'main-alert',
        'LmRtZ',
        'oatEK',
        'alert-main',
        'GLizt'
    ];
    _0x501d = function () {
        return _0x209805;
    };
    return _0x501d();
}
function enabledLoad() {
    const _0x466e49 = _0x113d, _0x4a91cd = {
            'fPFeu': _0x466e49(0x180),
            'AfKKr': _0x466e49(0x165),
            'xGUqJ': _0x466e49(0x13d) + 's',
            'rJvee': _0x466e49(0x196),
            'AGlFp': _0x466e49(0x148)
        };
    document[_0x466e49(0x14f) + _0x466e49(0x16d) + 'me'](_0x4a91cd[_0x466e49(0x17c)])[-0x17 * -0x131 + 0x599 * -0x5 + 0x96][_0x466e49(0x16a)][_0x466e49(0x155)] = _0x4a91cd[_0x466e49(0x162)], document[_0x466e49(0x14f) + _0x466e49(0x16d) + 'me'](_0x4a91cd[_0x466e49(0x1a6)])[0x45d * -0x6 + 0x1d8a + -0xa * 0x56][_0x466e49(0x16a)][_0x466e49(0x155)] = _0x4a91cd[_0x466e49(0x152)], document[_0x466e49(0x14f) + _0x466e49(0x16d) + 'me'](_0x4a91cd[_0x466e49(0x18a)])[0x1e91 + -0x2 * 0x652 + -0x11ed][_0x466e49(0x16a)][_0x466e49(0x155)] = _0x4a91cd[_0x466e49(0x152)];
}
function disabledLoad() {
    const _0x335b63 = _0x113d, _0x920081 = {
            'vOvnE': _0x335b63(0x180),
            'lIOEi': _0x335b63(0x165),
            'OxEZL': _0x335b63(0x13d) + 's',
            'ciHyp': _0x335b63(0x148)
        };
    document[_0x335b63(0x14f) + _0x335b63(0x16d) + 'me'](_0x920081[_0x335b63(0x16f)])[0xa3 * -0x10 + 0x2de * 0x4 + 0x1 * -0x148][_0x335b63(0x16a)][_0x335b63(0x155)] = _0x920081[_0x335b63(0x18c)], document[_0x335b63(0x14f) + _0x335b63(0x16d) + 'me'](_0x920081[_0x335b63(0x176)])[0x13e8 + -0xdd7 + -0x611 * 0x1][_0x335b63(0x16a)][_0x335b63(0x155)] = _0x920081[_0x335b63(0x18c)], document[_0x335b63(0x14f) + _0x335b63(0x16d) + 'me'](_0x920081[_0x335b63(0x193)])[-0x1fb7 * -0x1 + 0x2 * -0x78d + -0x109d][_0x335b63(0x16a)][_0x335b63(0x155)] = _0x920081[_0x335b63(0x18c)];
}
function extractResponseValue(_0x37ec77) {
    const _0x546aff = _0x113d, _0x4d8e1a = {
            'gqfdM': function (_0x2e0ed8, _0x41430d) {
                return _0x2e0ed8 >= _0x41430d;
            }
        }, _0x4b284f = /"response"\s*:\s*"([^"]+)"/, _0x5a40b6 = _0x37ec77[_0x546aff(0x170)](_0x4b284f);
    return _0x5a40b6 && _0x4d8e1a[_0x546aff(0x17a)](_0x5a40b6[_0x546aff(0x1a7)], 0x6 + -0x10c + 0x108) ? _0x5a40b6[-0x1 * 0x1261 + 0x2228 + -0xfc6] : null;
}
function encodedBase64(_0x4c7fb6) {
    const _0x1cc7c4 = _0x113d, _0xe4b234 = {
            'ojtwL': function (_0x370445, _0x599918) {
                return _0x370445(_0x599918);
            }
        }, _0x4c17ee = _0xe4b234[_0x1cc7c4(0x197)](btoa, _0x4c7fb6[_0x1cc7c4(0x18b)]);
    return _0x4c17ee;
}
function decodeBase64(_0x4f9487) {
    const _0x21d086 = _0x113d, _0x12fa41 = {
            'TkTTR': function (_0x1a362f, _0xd2866d) {
                return _0x1a362f(_0xd2866d);
            }
        }, _0x3ec64c = _0x12fa41[_0x21d086(0x175)](atob, _0x4f9487);
    return _0x3ec64c;
}
function saveDataInChrome(_0x2ad677, _0x17b5a2) {
    const _0x482687 = _0x113d, _0x31da61 = {};
    _0x31da61[_0x2ad677] = _0x17b5a2, chrome[_0x482687(0x1a8)][_0x482687(0x1ac)][_0x482687(0x15c)](_0x31da61, function () {
    });
}
async function loadDataInChrome(_0x19d687) {
    const _0x183174 = {
            'rTqBX': function (_0x1ba0f0, _0x2dbb88) {
                return _0x1ba0f0(_0x2dbb88);
            }
        }, _0x43d25d = await new Promise(_0x51c349 => {
            const _0x1bbc6d = _0x113d;
            chrome[_0x1bbc6d(0x1a8)][_0x1bbc6d(0x1ac)][_0x1bbc6d(0x144)](_0x19d687, function (_0x5acfb5) {
                const _0x54bbaa = _0x1bbc6d;
                _0x183174[_0x54bbaa(0x16b)](_0x51c349, _0x5acfb5);
            });
        });
    return _0x43d25d;
}
function saveDataStorage(_0x4bfcdf, _0x33add0) {
    const _0x124a1c = _0x113d;
    localStorage[_0x124a1c(0x161)](_0x4bfcdf, JSON[_0x124a1c(0x181)](_0x33add0));
}
function loadDataStorage(_0x24a9a4) {
    const _0x43a4a6 = _0x113d, _0x5ddcbe = {
            'EWhRf': function (_0x7ce195, _0x98342a) {
                return _0x7ce195 !== _0x98342a;
            }
        };
    if (_0x5ddcbe[_0x43a4a6(0x17f)](localStorage[_0x43a4a6(0x173)](_0x24a9a4), null))
        var _0x344451 = !![], _0xcac3f1 = JSON[_0x43a4a6(0x14c)](localStorage[_0x43a4a6(0x173)](_0x24a9a4));
    else
        var _0x344451 = ![], _0xcac3f1 = {};
    return {
        'status': _0x344451,
        'data': _0xcac3f1
    };
}
function sleep(_0x584ed1) {
    return new Promise(_0x57eaf5 => setTimeout(_0x57eaf5, _0x584ed1));
}
function formatCurrencyBrazilian(_0x2da1f4) {
    const _0x3dec00 = _0x113d, _0xc316d9 = {
            'SIPbo': function (_0x241915, _0x12f24b) {
                return _0x241915(_0x12f24b);
            },
            'NJHNC': _0x3dec00(0x160),
            'GwFqz': _0x3dec00(0x168),
            'NWOyK': _0x3dec00(0x15f)
        }, _0x10c8b6 = _0xc316d9[_0x3dec00(0x153)](Number, _0x2da1f4)[_0x3dec00(0x143) + _0x3dec00(0x186)](_0xc316d9[_0x3dec00(0x145)], {
            'style': _0xc316d9[_0x3dec00(0x19c)],
            'currency': _0xc316d9[_0x3dec00(0x1a0)],
            'minimumFractionDigits': 0x2
        });
    return _0x10c8b6;
}
function formatedCpf(_0x54e8b7) {
    const _0x50e691 = _0x113d, _0x4de906 = {
            'nIIzr': function (_0x268d20, _0x43f341) {
                return _0x268d20 != _0x43f341;
            },
            'YFIwV': _0x50e691(0x195),
            'ryTiu': _0x50e691(0x159)
        };
    return _0x4de906[_0x50e691(0x18f)](_0x54e8b7, '') && (_0x54e8b7 = _0x54e8b7[_0x50e691(0x182)](/\D/g, ''), _0x54e8b7 = _0x54e8b7[_0x50e691(0x182)](/(\d{3})(\d)/, _0x4de906[_0x50e691(0x188)]), _0x54e8b7 = _0x54e8b7[_0x50e691(0x182)](/(\d{3})(\d)/, _0x4de906[_0x50e691(0x188)]), _0x54e8b7 = _0x54e8b7[_0x50e691(0x182)](/(\d{3})(\d{1,2})$/, _0x4de906[_0x50e691(0x142)])), _0x54e8b7;
}
function _0x113d(_0x593d2a, _0xa6f84b) {
    const _0x4abc67 = _0x501d();
    return _0x113d = function (_0x4341bc, _0x102f16) {
        _0x4341bc = _0x4341bc - (-0x2dd * 0x2 + -0x1a3e * 0x1 + -0xfa * -0x22);
        let _0x5acf76 = _0x4abc67[_0x4341bc];
        return _0x5acf76;
    }, _0x113d(_0x593d2a, _0xa6f84b);
}
function formatedPhone(_0x2893ea) {
    const _0x53ec6b = _0x113d, _0x1a114b = {
            'ZUiLR': function (_0x4addf0, _0x4e303d) {
                return _0x4addf0 != _0x4e303d;
            },
            'XgVQF': _0x53ec6b(0x156),
            'RJXCE': _0x53ec6b(0x159)
        };
    return _0x1a114b[_0x53ec6b(0x172)](_0x2893ea, '') && (_0x2893ea = _0x2893ea[_0x53ec6b(0x182)](/\D/g, ''), _0x2893ea = _0x2893ea[_0x53ec6b(0x182)](/(\d{2})(\d)/, _0x1a114b[_0x53ec6b(0x16c)]), _0x2893ea = _0x2893ea[_0x53ec6b(0x182)](/(\d{5})(\d)/, _0x1a114b[_0x53ec6b(0x167)])), _0x2893ea;
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