# Changelog

## 1.5.0 (2025-10-08)

Full Changelog: [v1.4.1-alpha.0...v1.5.0](https://github.com/plastic-labs/honcho-python-core/compare/v1.4.1-alpha.0...v1.5.0)

### Features

* **api:** api update ([641c510](https://github.com/plastic-labs/honcho-python-core/commit/641c510efe158915b04e3a1eac14a427c94f3fe4))
* **api:** manual updates ([7314f79](https://github.com/plastic-labs/honcho-python-core/commit/7314f79200b2532afd77c830d0709c9ea75f6cff))

## 1.4.1-alpha.0 (2025-10-01)

Full Changelog: [v1.4.0...v1.4.1-alpha.0](https://github.com/plastic-labs/honcho-python-core/compare/v1.4.0...v1.4.1-alpha.0)

### Features

* **api:** Peer Card ([23165e4](https://github.com/plastic-labs/honcho-python-core/commit/23165e4e8563d7709a9acf5aec6d64b49ce2a882))
* improve future compat with pydantic v3 ([1242869](https://github.com/plastic-labs/honcho-python-core/commit/1242869e64af91f4c7869d054bfbe27bc4225afb))
* **types:** replace List[str] with SequenceNotStr in params ([00506c5](https://github.com/plastic-labs/honcho-python-core/commit/00506c5dbc93a07cfeeaa6ccc140ee6706c165e6))


### Bug Fixes

* avoid newer type syntax ([06235d3](https://github.com/plastic-labs/honcho-python-core/commit/06235d3f0d00f2a52de7f5c7924c9dd6d21f78b7))


### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([81c7134](https://github.com/plastic-labs/honcho-python-core/commit/81c7134ce09a10882a738426ebf169932031ee59))
* **internal:** add Sequence related utils ([2bd5ae1](https://github.com/plastic-labs/honcho-python-core/commit/2bd5ae146695d895b54ef0162714259bd44494b5))
* **internal:** change ci workflow machines ([47cb48f](https://github.com/plastic-labs/honcho-python-core/commit/47cb48f5a988977e086df6473ccdb165a258abe3))
* **internal:** move mypy configurations to `pyproject.toml` file ([08dfab1](https://github.com/plastic-labs/honcho-python-core/commit/08dfab1db0787ae287ad20e7209cc293783e8a1d))
* **internal:** update pydantic dependency ([53e807b](https://github.com/plastic-labs/honcho-python-core/commit/53e807b7d1532fcb451e0c98c0c5b8bbef7c8e71))
* **internal:** update pyright exclude list ([fbd6db0](https://github.com/plastic-labs/honcho-python-core/commit/fbd6db01b757d1b76b2b39c1e38d0d377051ac4b))
* **tests:** simplify `get_platform` test ([9e86700](https://github.com/plastic-labs/honcho-python-core/commit/9e8670024fe4c2c3534ef5a93d67b1c5d6ebb901))
* **types:** change optional parameter type from NotGiven to Omit ([f65c26a](https://github.com/plastic-labs/honcho-python-core/commit/f65c26a4710885df21166ede7d9d4590dd00af76))
* update github action ([11362ac](https://github.com/plastic-labs/honcho-python-core/commit/11362acaa7df7b01c1c7bf618f48a8ae0ae8a1cf))

## 1.4.0 (2025-08-12)

Full Changelog: [v1.3.0...v1.4.0](https://github.com/plastic-labs/honcho-python-core/compare/v1.3.0...v1.4.0)

### Features

* **api:** manual updates ([cc401f3](https://github.com/plastic-labs/honcho-python-core/commit/cc401f33cf29d3d9e7368b421c59088c28cf0ec8))
* **api:** manual updates ([ffa0cb1](https://github.com/plastic-labs/honcho-python-core/commit/ffa0cb18fd084729c30f2f723cc3287103e1edd0))
* **api:** Update Session Context ([8a2a705](https://github.com/plastic-labs/honcho-python-core/commit/8a2a705dca58f86b996f3110921a84d9763c66c5))


### Chores

* **internal:** update comment in script ([6c35b7f](https://github.com/plastic-labs/honcho-python-core/commit/6c35b7f9c214522f44cb8190b3f93ae91376f5d5))
* update @stainless-api/prism-cli to v5.15.0 ([e5645fc](https://github.com/plastic-labs/honcho-python-core/commit/e5645fc3ac7d714de56bfc0f1e834fea38a7ae84))

## 1.3.0 (2025-08-06)

Full Changelog: [v1.2.0...v1.3.0](https://github.com/plastic-labs/honcho-python-core/compare/v1.2.0...v1.3.0)

### Features

* **api:** manual updates ([a4637f5](https://github.com/plastic-labs/honcho-python-core/commit/a4637f5df79b0025ff2f446859256a8b363454d2))
* **api:** manual updates ([d78eedd](https://github.com/plastic-labs/honcho-python-core/commit/d78eedd64878ab3dbf2ba1d86a7da1a0342d1e81))
* **api:** pluralize filter*s* everywhere for consistency ([9883c7c](https://github.com/plastic-labs/honcho-python-core/commit/9883c7c930a29119016bebab2689a58b46b0329e))
* **client:** support file upload requests ([0f96184](https://github.com/plastic-labs/honcho-python-core/commit/0f961844ed4e782ddc58496c292c18762ad4b144))


### Bug Fixes

* **parsing:** ignore empty metadata ([c5a84e3](https://github.com/plastic-labs/honcho-python-core/commit/c5a84e3d14f1f4235efcb79813dd0640c8bba96d))
* **parsing:** parse extra field types ([88bdac0](https://github.com/plastic-labs/honcho-python-core/commit/88bdac087da3dd1cae6170ec41be398b165e018b))


### Chores

* **internal:** fix ruff target version ([a667674](https://github.com/plastic-labs/honcho-python-core/commit/a667674311761f01f183f82c65e07d144f4dc14c))
* **project:** add settings file for vscode ([c54f786](https://github.com/plastic-labs/honcho-python-core/commit/c54f7860ab62b07ea5dcb10e66296804339f2b9d))
* remove custom code ([de6327d](https://github.com/plastic-labs/honcho-python-core/commit/de6327d2e9ae4e7d8d2bc419139e47dc9d315117))

## 1.2.0 (2025-07-16)

Full Changelog: [v1.1.0...v1.2.0](https://github.com/plastic-labs/honcho-python-core/compare/v1.1.0...v1.2.0)

### Features

* **api:** manual updates ([9cf149f](https://github.com/plastic-labs/honcho-python-core/commit/9cf149fd36ca429cbf6ca2a880735a29ca9aa736))
* **api:** manual updates ([8b91a94](https://github.com/plastic-labs/honcho-python-core/commit/8b91a940df27e96de8ba004871ea9a304b7bdad3))
* **api:** manual updates ([24d5066](https://github.com/plastic-labs/honcho-python-core/commit/24d50661ead4916896b2c25d3c93c25c6de608c1))
* **api:** manual updates -- add file upload endpoints ([6393896](https://github.com/plastic-labs/honcho-python-core/commit/6393896c740603b5e833edf91e6e75493d840145))
* clean up environment call outs ([f92dab9](https://github.com/plastic-labs/honcho-python-core/commit/f92dab93e4321bd8e4c8e98bc8303d00eaf0a426))


### Bug Fixes

* **ci:** correct conditional ([246a6eb](https://github.com/plastic-labs/honcho-python-core/commit/246a6eb5eebccece80c19d434e4e9cf896eaa2c6))
* **ci:** release-doctor — report correct token name ([f3c44e3](https://github.com/plastic-labs/honcho-python-core/commit/f3c44e340fc7a2b60137e0a3185aea892b734806))
* **client:** don't send Content-Type header on GET requests ([88597e4](https://github.com/plastic-labs/honcho-python-core/commit/88597e413ff52bafbe3819ce40432b535f390cb2))
* **parsing:** correctly handle nested discriminated unions ([1862c6d](https://github.com/plastic-labs/honcho-python-core/commit/1862c6d1ceb2f82199d1f29bca56118df6d475d6))


### Chores

* **ci:** change upload type ([0ba882f](https://github.com/plastic-labs/honcho-python-core/commit/0ba882fe8c0c0ed554dcc0173a91fe1c2229b652))
* **ci:** only run for pushes and fork pull requests ([10c2fc7](https://github.com/plastic-labs/honcho-python-core/commit/10c2fc780f1963a515435a706e603f66c32d79f0))
* **internal:** bump pinned h11 dep ([53c88c2](https://github.com/plastic-labs/honcho-python-core/commit/53c88c2ae0958811485140c3adc938a8f830c730))
* **internal:** codegen related update ([e37634f](https://github.com/plastic-labs/honcho-python-core/commit/e37634f2e868664513bfe8b58a42bf0f8d7697f2))
* **package:** mark python 3.13 as supported ([999dcc3](https://github.com/plastic-labs/honcho-python-core/commit/999dcc30daf3bf3d62d9242321fca4da8546da21))
* **readme:** fix version rendering on pypi ([9d9391f](https://github.com/plastic-labs/honcho-python-core/commit/9d9391fa1d303123d4727087bd168a78b850f588))

## 1.1.0 (2025-06-26)

Full Changelog: [v1.0.1...v1.1.0](https://github.com/plastic-labs/honcho-python-core/compare/v1.0.1...v1.1.0)

### Features

* **api:** manual updates ([f5ab5f7](https://github.com/plastic-labs/honcho-python-core/commit/f5ab5f7cb72eebf360b638e3227e7fe952be8a93))
* **api:** manual updates ([350d42d](https://github.com/plastic-labs/honcho-python-core/commit/350d42d1b7a6fc292f5336c4723aa247f7f5ae15))
* **client:** add support for aiohttp ([263b57f](https://github.com/plastic-labs/honcho-python-core/commit/263b57f16f9d792a750424f313d2543743a51e8d))


### Chores

* **tests:** skip some failing tests on the latest python versions ([72f94e0](https://github.com/plastic-labs/honcho-python-core/commit/72f94e03ba07b5983e8c87106aba2d46b855dc96))

## 1.0.1 (2025-06-19)

Full Changelog: [v1.0.0...v1.0.1](https://github.com/plastic-labs/honcho-python-core/compare/v1.0.0...v1.0.1)

### Features

* **api:** change package name ([cd57239](https://github.com/plastic-labs/honcho-python-core/commit/cd57239edac29005febf65ffac274fb27024307b))

## 1.0.0 (2025-06-19)

Full Changelog: [v0.2.0...v1.0.0](https://github.com/plastic-labs/honcho-python-core/compare/v0.2.0...v1.0.0)

### Features

* **api:** manual updates ([467ea24](https://github.com/plastic-labs/honcho-python-core/commit/467ea247202d8ae78bdf62a02221d64af470d99d))
* **api:** manual updates ([2759773](https://github.com/plastic-labs/honcho-python-core/commit/27597730108b1ac2e554eb6ab789de15a907efbb))
* **api:** rewrite to peer paradigm ([5e2b28c](https://github.com/plastic-labs/honcho-python-core/commit/5e2b28c3fecca7c1cfffe2604066785a243e8f5b))
* **client:** add follow_redirects request option ([a67087d](https://github.com/plastic-labs/honcho-python-core/commit/a67087d57139eca2156c81f20ce8e48ad6191c03))


### Bug Fixes

* **client:** correctly parse binary response | stream ([cbe4470](https://github.com/plastic-labs/honcho-python-core/commit/cbe4470d68ffc8109e2fb1630eac8a9c84efa343))
* **docs/api:** remove references to nonexistent types ([ccfcd32](https://github.com/plastic-labs/honcho-python-core/commit/ccfcd3200531027cb5ebeed448663fd999bd8ce8))
* **pagination:** correct next page check ([c32d3c8](https://github.com/plastic-labs/honcho-python-core/commit/c32d3c8d06393664d182b6647cf21c9d069cf159))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([e4ad948](https://github.com/plastic-labs/honcho-python-core/commit/e4ad9482da0b352525b5bc646fb28d4d44735f51))


### Chores

* **ci:** enable for pull requests ([8727464](https://github.com/plastic-labs/honcho-python-core/commit/8727464315f8e3c92aa6f782211255667215cfbb))
* **ci:** fix installation instructions ([1b96727](https://github.com/plastic-labs/honcho-python-core/commit/1b967270a5a01bb7448da46b516d53f57fa13459))
* **docs:** grammar improvements ([a7df346](https://github.com/plastic-labs/honcho-python-core/commit/a7df3462af1393974722741784f37c36eb77d768))
* **docs:** remove reference to rye shell ([8bf0600](https://github.com/plastic-labs/honcho-python-core/commit/8bf06005f6145e9e975faf9eb1ae6f7da55cc395))
* **internal:** update conftest.py ([34853e1](https://github.com/plastic-labs/honcho-python-core/commit/34853e196e711efb8639c614b9f7aa442de5f2dd))
* **readme:** update badges ([8c783f4](https://github.com/plastic-labs/honcho-python-core/commit/8c783f4488be656b7d0b5f2ba2c1280e1a2fcc2e))
* **tests:** add tests for httpx client instantiation & proxies ([79cbe9d](https://github.com/plastic-labs/honcho-python-core/commit/79cbe9df0a3da4344f8fbd92af6b44d3405de19c))
* **tests:** run tests in parallel ([1e601cc](https://github.com/plastic-labs/honcho-python-core/commit/1e601cc23c490f9310e9df904e10314b3f13e556))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([def0a0c](https://github.com/plastic-labs/honcho-python-core/commit/def0a0cdc1785e52521af9a64d5157da644114a2))

## 0.2.0 (2025-05-15)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/plastic-labs/honcho-python/compare/v0.1.0...v0.2.0)

### Features

* **api:** api update ([8b5345b](https://github.com/plastic-labs/honcho-python/commit/8b5345bfd27696fc100fdc88cd9c13c8f3bf2867))


### Bug Fixes

* **package:** support direct resource imports ([115cfeb](https://github.com/plastic-labs/honcho-python/commit/115cfeb619e2663af9f96985e0f315a506fe5bf6))
* **perf:** optimize some hot paths ([cdda641](https://github.com/plastic-labs/honcho-python/commit/cdda6419061216c4a1a5dd5a13cca464d0497323))
* **perf:** skip traversing types for NotGiven values ([e98b470](https://github.com/plastic-labs/honcho-python/commit/e98b470891968a1244f7f6e10938a56d50fc4f7c))
* **pydantic v1:** more robust ModelField.annotation check ([3705ebb](https://github.com/plastic-labs/honcho-python/commit/3705ebb7f325447daec9167c6a5c13d3fda4e514))


### Chores

* broadly detect json family of content-type headers ([4edaae5](https://github.com/plastic-labs/honcho-python/commit/4edaae507778ee9a9d480c915cd0bde9ecbeb275))
* **ci:** add timeout thresholds for CI jobs ([37ffc48](https://github.com/plastic-labs/honcho-python/commit/37ffc480001e68df382d6fab12aeaf28454586dd))
* **ci:** only use depot for staging repos ([8112338](https://github.com/plastic-labs/honcho-python/commit/81123387b5496a0ecba4adf08ead3724a27709bf))
* **ci:** upload sdks to package manager ([1715d2a](https://github.com/plastic-labs/honcho-python/commit/1715d2af06a0d8495f15027e8bf9f110c15ffc35))
* **client:** minor internal fixes ([3c2cd66](https://github.com/plastic-labs/honcho-python/commit/3c2cd66a3b95c803d9cff8daaa3dd6ede789d929))
* **internal:** avoid errors for isinstance checks on proxies ([fbbd3c1](https://github.com/plastic-labs/honcho-python/commit/fbbd3c1068a1af6639cd0ab4095bad5fc44fd321))
* **internal:** base client updates ([8c4985d](https://github.com/plastic-labs/honcho-python/commit/8c4985d2ee0b56899c4e17e8028c48fd0c976c30))
* **internal:** bump pyright version ([f672b94](https://github.com/plastic-labs/honcho-python/commit/f672b94d6d0c92f69f6416fdd44b69f70bb327ca))
* **internal:** codegen related update ([8644872](https://github.com/plastic-labs/honcho-python/commit/8644872ec648b5705cda992af42b3190388ec20d))
* **internal:** fix list file params ([6fa0c14](https://github.com/plastic-labs/honcho-python/commit/6fa0c141c1dfc40666d4c99227e69ffb65943770))
* **internal:** import reformatting ([3b79ce8](https://github.com/plastic-labs/honcho-python/commit/3b79ce84d59520a30cf7d37f45ba1cd509fe0114))
* **internal:** minor formatting changes ([2006925](https://github.com/plastic-labs/honcho-python/commit/2006925d2c90a7a85739d12de167c3238942d82b))
* **internal:** refactor retries to not use recursion ([fc856e3](https://github.com/plastic-labs/honcho-python/commit/fc856e3a04283fb030d00d4b736054ab599d06c6))
* **internal:** update models test ([e98feff](https://github.com/plastic-labs/honcho-python/commit/e98feff770b4669d5c6e49a389af3352af9f4353))
* **internal:** update pyright settings ([3d2ec51](https://github.com/plastic-labs/honcho-python/commit/3d2ec51a09e4548da3ea3bbd149a2f47a6e665d9))

## 0.1.0 (2025-04-10)

Full Changelog: [v0.0.19...v0.1.0](https://github.com/plastic-labs/honcho-python/compare/v0.0.19...v0.1.0)

### Features

* **api:** api update ([6f06951](https://github.com/plastic-labs/honcho-python/commit/6f069513e70b3a3600deb09e8eb021337944569f))
* **client:** allow passing `NotGiven` for body ([#106](https://github.com/plastic-labs/honcho-python/issues/106)) ([8b7fb6b](https://github.com/plastic-labs/honcho-python/commit/8b7fb6ba38fe527fb9eebdbbfbefdee885145d48))
* **client:** send `X-Stainless-Read-Timeout` header ([#101](https://github.com/plastic-labs/honcho-python/issues/101)) ([9814119](https://github.com/plastic-labs/honcho-python/commit/98141199db4f5ccfa07e704023875941e0c0c397))
* remove examples ([#122](https://github.com/plastic-labs/honcho-python/issues/122)) ([93451b9](https://github.com/plastic-labs/honcho-python/commit/93451b95c68a66d6abc57c9185ee7eec144d4118))


### Bug Fixes

* asyncify on non-asyncio runtimes ([#105](https://github.com/plastic-labs/honcho-python/issues/105)) ([fd19273](https://github.com/plastic-labs/honcho-python/commit/fd192732afe460e3843542a05a33a775d2c946d9))
* **ci:** ensure pip is always available ([#117](https://github.com/plastic-labs/honcho-python/issues/117)) ([99f6142](https://github.com/plastic-labs/honcho-python/commit/99f6142afa56e29f53f365d2e6e38f3af411e2fd))
* **ci:** remove publishing patch ([#118](https://github.com/plastic-labs/honcho-python/issues/118)) ([b74fc9c](https://github.com/plastic-labs/honcho-python/commit/b74fc9c518837ca26a1a718fddf65b35d1595186))
* **client:** mark some request bodies as optional ([8b7fb6b](https://github.com/plastic-labs/honcho-python/commit/8b7fb6ba38fe527fb9eebdbbfbefdee885145d48))
* **client:** only call .close() when needed ([#90](https://github.com/plastic-labs/honcho-python/issues/90)) ([91d9a14](https://github.com/plastic-labs/honcho-python/commit/91d9a14b38aedb049519fd7a846147c0a1535e87))
* correctly handle deserialising `cls` fields ([#92](https://github.com/plastic-labs/honcho-python/issues/92)) ([b42d933](https://github.com/plastic-labs/honcho-python/commit/b42d933fc3aec7b2afb352f1cf10fdf52ae0f535))
* **tests:** make test_get_platform less flaky ([#95](https://github.com/plastic-labs/honcho-python/issues/95)) ([9ad9881](https://github.com/plastic-labs/honcho-python/commit/9ad98812262b9b4b8f401ea40d960e3c15692acc))
* **types:** handle more discriminated union shapes ([#116](https://github.com/plastic-labs/honcho-python/issues/116)) ([fac82e7](https://github.com/plastic-labs/honcho-python/commit/fac82e713058f0d05db7c227751e2c0ecf79d438))


### Chores

* add missing isclass check ([#88](https://github.com/plastic-labs/honcho-python/issues/88)) ([a749def](https://github.com/plastic-labs/honcho-python/commit/a749def9b78cc9258624e753c21b699bcb343e9a))
* **docs:** update client docstring ([#110](https://github.com/plastic-labs/honcho-python/issues/110)) ([5b44617](https://github.com/plastic-labs/honcho-python/commit/5b446172b4d6bcf7ace1063f2e1eb6e06e821f45))
* fix typos ([#119](https://github.com/plastic-labs/honcho-python/issues/119)) ([dcd0342](https://github.com/plastic-labs/honcho-python/commit/dcd03424af3f5b676ba6753954b3c313feddfda3))
* **internal:** avoid pytest-asyncio deprecation warning ([#96](https://github.com/plastic-labs/honcho-python/issues/96)) ([ffb58cc](https://github.com/plastic-labs/honcho-python/commit/ffb58cc8a84f2d5555e14c7bc9a270521f04cda0))
* **internal:** bummp ruff dependency ([#100](https://github.com/plastic-labs/honcho-python/issues/100)) ([c5a9683](https://github.com/plastic-labs/honcho-python/commit/c5a96836b00dc6b0fef09c5aa18f17ff461e9236))
* **internal:** bump httpx dependency ([#89](https://github.com/plastic-labs/honcho-python/issues/89)) ([39eeb9c](https://github.com/plastic-labs/honcho-python/commit/39eeb9c588d1618425a92541102785bc0503163c))
* **internal:** bump rye to 0.44.0 ([#115](https://github.com/plastic-labs/honcho-python/issues/115)) ([48df477](https://github.com/plastic-labs/honcho-python/commit/48df477d323ee01a62d6dcd9667536660d72e924))
* **internal:** change default timeout to an int ([#99](https://github.com/plastic-labs/honcho-python/issues/99)) ([7fcb6d0](https://github.com/plastic-labs/honcho-python/commit/7fcb6d052cdcfd831a97953eeb5cc308187ee821))
* **internal:** codegen related update ([#114](https://github.com/plastic-labs/honcho-python/issues/114)) ([083a5fc](https://github.com/plastic-labs/honcho-python/commit/083a5fcd14857c467c281591557fd962c156a8a3))
* **internal:** codegen related update ([#80](https://github.com/plastic-labs/honcho-python/issues/80)) ([8b0da45](https://github.com/plastic-labs/honcho-python/commit/8b0da45454d25c06d128a2c9c9db6f5a2f4d79ab))
* **internal:** codegen related update ([#81](https://github.com/plastic-labs/honcho-python/issues/81)) ([a01befa](https://github.com/plastic-labs/honcho-python/commit/a01befac4dca887e142a1385ddc056e519090582))
* **internal:** codegen related update ([#86](https://github.com/plastic-labs/honcho-python/issues/86)) ([5395eca](https://github.com/plastic-labs/honcho-python/commit/5395ecaff9e7fcfec1cfc827b21607313cfc911f))
* **internal:** codegen related update ([#87](https://github.com/plastic-labs/honcho-python/issues/87)) ([412b55f](https://github.com/plastic-labs/honcho-python/commit/412b55fb329e94a84afd48a592cdd98ee40a94b7))
* **internal:** codegen related update ([#91](https://github.com/plastic-labs/honcho-python/issues/91)) ([8faa186](https://github.com/plastic-labs/honcho-python/commit/8faa186233111bb99e53e206dd0d4d0518c6dc3f))
* **internal:** codegen related update ([#93](https://github.com/plastic-labs/honcho-python/issues/93)) ([7ad0afb](https://github.com/plastic-labs/honcho-python/commit/7ad0afb109d4e4e0cc2d1b0bf6b9a3a06a87e40e))
* **internal:** codegen related update ([#97](https://github.com/plastic-labs/honcho-python/issues/97)) ([ebda645](https://github.com/plastic-labs/honcho-python/commit/ebda6458059f5fcec2a495f92dbda7c2a20b0c36))
* **internal:** expand CI branch coverage ([cd01661](https://github.com/plastic-labs/honcho-python/commit/cd01661ef67fb93f81a739c4b2e6ad4a2260fa97))
* **internal:** fix devcontainers setup ([#107](https://github.com/plastic-labs/honcho-python/issues/107)) ([c589730](https://github.com/plastic-labs/honcho-python/commit/c589730df9acf0955db8749aed34c2366f9f1f4b))
* **internal:** fix type traversing dictionary params ([#102](https://github.com/plastic-labs/honcho-python/issues/102)) ([a3bd160](https://github.com/plastic-labs/honcho-python/commit/a3bd160890e39d2267d20316d10bf08a5ffdd116))
* **internal:** minor formatting changes ([#98](https://github.com/plastic-labs/honcho-python/issues/98)) ([ac3ec2d](https://github.com/plastic-labs/honcho-python/commit/ac3ec2d712b388da277f502e06e584142e430fcb))
* **internal:** minor type handling changes ([#103](https://github.com/plastic-labs/honcho-python/issues/103)) ([57363e7](https://github.com/plastic-labs/honcho-python/commit/57363e77e63dc8315a89a4e52e16d1122eda4493))
* **internal:** properly set __pydantic_private__ ([#108](https://github.com/plastic-labs/honcho-python/issues/108)) ([f9d6339](https://github.com/plastic-labs/honcho-python/commit/f9d63398ac3bc77946d3b2376ffc799d769bd67a))
* **internal:** reduce CI branch coverage ([fe9c3c5](https://github.com/plastic-labs/honcho-python/commit/fe9c3c59a14c0f1bdab364ec9da1637229948386))
* **internal:** remove extra empty newlines ([#113](https://github.com/plastic-labs/honcho-python/issues/113)) ([ce17235](https://github.com/plastic-labs/honcho-python/commit/ce172350a6f2655af12b0ea05ddb371a0bb340f4))
* **internal:** remove trailing character ([#120](https://github.com/plastic-labs/honcho-python/issues/120)) ([513b256](https://github.com/plastic-labs/honcho-python/commit/513b256b6f59ca4998785a80744ecf32622b0255))
* **internal:** remove unused http client options forwarding ([#111](https://github.com/plastic-labs/honcho-python/issues/111)) ([09b4ed4](https://github.com/plastic-labs/honcho-python/commit/09b4ed4cc8d497876c1db4e31f1119c281f016e9))
* **internal:** slight transform perf improvement ([#121](https://github.com/plastic-labs/honcho-python/issues/121)) ([0dabda8](https://github.com/plastic-labs/honcho-python/commit/0dabda85033a93372b8e0d0c3aaff75102f5fae0))
* **internal:** update client tests ([#104](https://github.com/plastic-labs/honcho-python/issues/104)) ([6cd7632](https://github.com/plastic-labs/honcho-python/commit/6cd7632e4f581908eaa9e8a3716376507c937d78))


### Documentation

* **raw responses:** fix duplicate `the` ([#94](https://github.com/plastic-labs/honcho-python/issues/94)) ([d093719](https://github.com/plastic-labs/honcho-python/commit/d093719615bc9aa996515c579bdc9965e355ab33))
* **readme:** example snippet for client context manager ([#85](https://github.com/plastic-labs/honcho-python/issues/85)) ([5104481](https://github.com/plastic-labs/honcho-python/commit/510448166eb83ba17f4da2bcacaf7575cbba63fd))
* update URLs from stainlessapi.com to stainless.com ([#109](https://github.com/plastic-labs/honcho-python/issues/109)) ([9e24d1e](https://github.com/plastic-labs/honcho-python/commit/9e24d1ea515d1b55c4d4ff1abf9c29ca48cd54b5))

## 0.0.19 (2024-12-16)

Full Changelog: [v0.0.18...v0.0.19](https://github.com/plastic-labs/honcho-python/compare/v0.0.18...v0.0.19)

### Features

* **api:** api update ([#82](https://github.com/plastic-labs/honcho-python/issues/82)) ([f295a74](https://github.com/plastic-labs/honcho-python/commit/f295a748dd5a168878b14515b5601d462f56a9d8))


### Chores

* **internal:** add support for TypeAliasType ([#78](https://github.com/plastic-labs/honcho-python/issues/78)) ([66e0d96](https://github.com/plastic-labs/honcho-python/commit/66e0d96e66ec4981bf2cd31eb717eff80fde9041))
* **internal:** bump pydantic dependency ([#74](https://github.com/plastic-labs/honcho-python/issues/74)) ([43ea1de](https://github.com/plastic-labs/honcho-python/commit/43ea1dec3ad6e2a28fd5cbe101a63201c8937f8a))
* **internal:** bump pyright ([#77](https://github.com/plastic-labs/honcho-python/issues/77)) ([b613832](https://github.com/plastic-labs/honcho-python/commit/b613832984ab0dbb5f82dc83808b679e87e6944e))
* **internal:** codegen related update ([#79](https://github.com/plastic-labs/honcho-python/issues/79)) ([62d7c38](https://github.com/plastic-labs/honcho-python/commit/62d7c38c172a8761b880a0eb7996d01737d3786f))
* **internal:** codegen related update ([#80](https://github.com/plastic-labs/honcho-python/issues/80)) ([e5b574e](https://github.com/plastic-labs/honcho-python/commit/e5b574e0b9897036ff2f06e725dc86492973a893))
* **internal:** codegen related update ([#81](https://github.com/plastic-labs/honcho-python/issues/81)) ([9a4cd72](https://github.com/plastic-labs/honcho-python/commit/9a4cd72e6225d2a70870b2f1853e98039747e55c))


### Documentation

* **readme:** fix http client proxies example ([#76](https://github.com/plastic-labs/honcho-python/issues/76)) ([30cacbf](https://github.com/plastic-labs/honcho-python/commit/30cacbf37ea84226175ccc1dcef2964a8e7392ad))

## 0.0.18 (2024-12-04)

Full Changelog: [v0.0.17...v0.0.18](https://github.com/plastic-labs/honcho-python/compare/v0.0.17...v0.0.18)

### Bug Fixes

* **client:** compat with new httpx 0.28.0 release ([#70](https://github.com/plastic-labs/honcho-python/issues/70)) ([ac37c4b](https://github.com/plastic-labs/honcho-python/commit/ac37c4bace9edaa3c8c73c293f9eaf555736f5ba))


### Chores

* **internal:** codegen related update ([#71](https://github.com/plastic-labs/honcho-python/issues/71)) ([9b037b4](https://github.com/plastic-labs/honcho-python/commit/9b037b4f43dbdffa6b090778bbc084f8f4880dc5))
* **internal:** exclude mypy from running on tests ([#69](https://github.com/plastic-labs/honcho-python/issues/69)) ([8b3801d](https://github.com/plastic-labs/honcho-python/commit/8b3801db9f42c3e78fca1721be3291f4a35c8528))
* **internal:** fix compat model_dump method when warnings are passed ([#66](https://github.com/plastic-labs/honcho-python/issues/66)) ([e80f5e7](https://github.com/plastic-labs/honcho-python/commit/e80f5e7b8d09ad63c2ac6d27aa9f150b5f77165d))
* make the `Omit` type public ([#72](https://github.com/plastic-labs/honcho-python/issues/72)) ([7ba4680](https://github.com/plastic-labs/honcho-python/commit/7ba46804dcab6b79560ec01f51b1062e6d0a2bd0))
* rebuild project due to codegen change ([#64](https://github.com/plastic-labs/honcho-python/issues/64)) ([6c86c34](https://github.com/plastic-labs/honcho-python/commit/6c86c343d24969a61cf8b0504e3b286b6380d380))
* remove now unused `cached-property` dep ([#68](https://github.com/plastic-labs/honcho-python/issues/68)) ([ba01875](https://github.com/plastic-labs/honcho-python/commit/ba01875143a8c5a63cb19a98e46b63663979e79d))


### Documentation

* add info log level to readme ([#67](https://github.com/plastic-labs/honcho-python/issues/67)) ([2482b6a](https://github.com/plastic-labs/honcho-python/commit/2482b6a83211edff3114485a7b085b320a08bbf0))

## 0.0.17 (2024-11-15)

Full Changelog: [v0.0.16...v0.0.17](https://github.com/plastic-labs/honcho-python/compare/v0.0.16...v0.0.17)

### Features

* **api:** api update ([#62](https://github.com/plastic-labs/honcho-python/issues/62)) ([3d0f092](https://github.com/plastic-labs/honcho-python/commit/3d0f0926388511a63279282784206fdb4f5fdb3d))


### Chores

* rebuild project due to codegen change ([#59](https://github.com/plastic-labs/honcho-python/issues/59)) ([c7617bc](https://github.com/plastic-labs/honcho-python/commit/c7617bc5e0dc029e47e40f478bbb69144f7eff8c))
* rebuild project due to codegen change ([#61](https://github.com/plastic-labs/honcho-python/issues/61)) ([315c96f](https://github.com/plastic-labs/honcho-python/commit/315c96f27ef449bc5c290b2d93432fcbfbe8a35b))

## 0.0.16 (2024-11-07)

Full Changelog: [v0.0.15...v0.0.16](https://github.com/plastic-labs/honcho-python/compare/v0.0.15...v0.0.16)

### Features

* **api:** Add cloning feature ([#57](https://github.com/plastic-labs/honcho-python/issues/57)) ([1ce2ea6](https://github.com/plastic-labs/honcho-python/commit/1ce2ea62e49b5cf896a2815d0cc5664fa4a581fc))


### Chores

* rebuild project due to codegen change ([#54](https://github.com/plastic-labs/honcho-python/issues/54)) ([8f99f6b](https://github.com/plastic-labs/honcho-python/commit/8f99f6b4a18d2c57975134dfe733232307022a69))
* rebuild project due to codegen change ([#56](https://github.com/plastic-labs/honcho-python/issues/56)) ([1a9f49e](https://github.com/plastic-labs/honcho-python/commit/1a9f49e88fbb65fe16d195f8db3ef9146db5678a))

## 0.0.15 (2024-10-21)

Full Changelog: [v0.0.14...v0.0.15](https://github.com/plastic-labs/honcho-python/compare/v0.0.14...v0.0.15)

### Features

* **api:** api update ([#49](https://github.com/plastic-labs/honcho-python/issues/49)) ([4bdb1cc](https://github.com/plastic-labs/honcho-python/commit/4bdb1ccaa307ab2073b4a74efd5ca7cf3882f857))
* **api:** api update ([#50](https://github.com/plastic-labs/honcho-python/issues/50)) ([e3a6935](https://github.com/plastic-labs/honcho-python/commit/e3a6935f3b48a2492799d8055c762c1f3e412f04))
* **api:** api update ([#51](https://github.com/plastic-labs/honcho-python/issues/51)) ([1811f82](https://github.com/plastic-labs/honcho-python/commit/1811f8227f12c4d6329dc63e36b9ba6b42ba1aa6))
* **api:** api update ([#52](https://github.com/plastic-labs/honcho-python/issues/52)) ([2dcfe26](https://github.com/plastic-labs/honcho-python/commit/2dcfe26f3f30278847761e6afa57ee085e142292))
* **api:** update via SDK Studio ([#45](https://github.com/plastic-labs/honcho-python/issues/45)) ([9bc721d](https://github.com/plastic-labs/honcho-python/commit/9bc721d1f607392ba823024a904a9ca7de151edd))


### Chores

* **internal:** codegen related update ([#43](https://github.com/plastic-labs/honcho-python/issues/43)) ([5a4d3a4](https://github.com/plastic-labs/honcho-python/commit/5a4d3a4acf768d48e7dc075166b07bb134f98f7b))
* **internal:** codegen related update ([#46](https://github.com/plastic-labs/honcho-python/issues/46)) ([2183d2b](https://github.com/plastic-labs/honcho-python/commit/2183d2b34597d61bdc3a7a5cd9082daa438654b2))


### Documentation

* **readme:** add section on determining installed version ([#47](https://github.com/plastic-labs/honcho-python/issues/47)) ([d765d26](https://github.com/plastic-labs/honcho-python/commit/d765d26845453095b8c364801e48ff15b71238be))
* update CONTRIBUTING.md ([#48](https://github.com/plastic-labs/honcho-python/issues/48)) ([bc577f6](https://github.com/plastic-labs/honcho-python/commit/bc577f6bcfb084170d7e6919e10d71244cd69518))

## 0.0.14 (2024-08-15)

Full Changelog: [v0.0.13...v0.0.14](https://github.com/plastic-labs/honcho-python/compare/v0.0.13...v0.0.14)

### Features

* **api:** update via SDK Studio ([#34](https://github.com/plastic-labs/honcho-python/issues/34)) ([0d56b07](https://github.com/plastic-labs/honcho-python/commit/0d56b07f8d3020798e16a1667d5a92d6f352db0b))
* **client:** add `retry_count` to raw response class ([#37](https://github.com/plastic-labs/honcho-python/issues/37)) ([3d634a9](https://github.com/plastic-labs/honcho-python/commit/3d634a9b9b453ce8093a3e8f844224aa49ddbf54))


### Chores

* **internal:** bump pyright ([#36](https://github.com/plastic-labs/honcho-python/issues/36)) ([50c53ec](https://github.com/plastic-labs/honcho-python/commit/50c53ecdf096f0244d778f1aeb2d289e95d4cfa4))
* **internal:** bump ruff version ([#39](https://github.com/plastic-labs/honcho-python/issues/39)) ([eab1ecb](https://github.com/plastic-labs/honcho-python/commit/eab1ecbb97ec7a417f78a5bba65f4bd29efa87e1))
* **internal:** codegen related update ([#41](https://github.com/plastic-labs/honcho-python/issues/41)) ([eb43b2a](https://github.com/plastic-labs/honcho-python/commit/eb43b2a465e9a9778a123b4e333ff93ad0912d55))
* **internal:** test updates ([#38](https://github.com/plastic-labs/honcho-python/issues/38)) ([026cca8](https://github.com/plastic-labs/honcho-python/commit/026cca816df8c9df9d6575a23e87f85690fdec10))
* **internal:** update pydantic compat helper function ([#40](https://github.com/plastic-labs/honcho-python/issues/40)) ([c25d82a](https://github.com/plastic-labs/honcho-python/commit/c25d82a07c610c363dfa9eea30ddb9b65561c64c))
* **internal:** use `TypeAlias` marker for type assignments ([#35](https://github.com/plastic-labs/honcho-python/issues/35)) ([fa192c7](https://github.com/plastic-labs/honcho-python/commit/fa192c7952034b6f667cb8dbf3223acbc0bf7cb2))
* **internal:** version bump ([#32](https://github.com/plastic-labs/honcho-python/issues/32)) ([78ce88f](https://github.com/plastic-labs/honcho-python/commit/78ce88fde8c1cd8acbe22e5f0c8792200b8c8c5e))

## 0.0.13 (2024-08-01)

Full Changelog: [v0.0.12...v0.0.13](https://github.com/plastic-labs/honcho-python/compare/v0.0.12...v0.0.13)

### Features

* **api:** OpenAPI spec update via Stainless API ([#31](https://github.com/plastic-labs/honcho-python/issues/31)) ([f626a2c](https://github.com/plastic-labs/honcho-python/commit/f626a2c303f866dcbb65237f2570d2ed9b064351))
* **api:** update via SDK Studio ([#24](https://github.com/plastic-labs/honcho-python/issues/24)) ([e5417f8](https://github.com/plastic-labs/honcho-python/commit/e5417f859174b237fa1c912188031b786842e0d6))
* **api:** update via SDK Studio ([#30](https://github.com/plastic-labs/honcho-python/issues/30)) ([f3e9cb4](https://github.com/plastic-labs/honcho-python/commit/f3e9cb49773691962b07067c531f288942711db1))


### Chores

* fix error message import example ([#28](https://github.com/plastic-labs/honcho-python/issues/28)) ([675f719](https://github.com/plastic-labs/honcho-python/commit/675f71940a184e8a277f6db8df2604d762bae1d5))
* **internal:** add type construction helper ([#29](https://github.com/plastic-labs/honcho-python/issues/29)) ([e526f46](https://github.com/plastic-labs/honcho-python/commit/e526f463dd0dea1a9047c11cf81366a06e1ed47b))
* **internal:** codegen related update ([#26](https://github.com/plastic-labs/honcho-python/issues/26)) ([8aa9cad](https://github.com/plastic-labs/honcho-python/commit/8aa9cad685d140c45ed9c01c4d8e853434352478))
* **tests:** update prism version ([#27](https://github.com/plastic-labs/honcho-python/issues/27)) ([0aa4203](https://github.com/plastic-labs/honcho-python/commit/0aa42032400a4dcff1f11086233074e080f3097c))

## 0.0.12 (2024-05-23)

Full Changelog: [v0.0.11...v0.0.12](https://github.com/plastic-labs/honcho-python/compare/v0.0.11...v0.0.12)

### Features

* **api:** update via SDK Studio ([#22](https://github.com/plastic-labs/honcho-python/issues/22)) ([a9e7757](https://github.com/plastic-labs/honcho-python/commit/a9e7757b02f4cd560d12717af38bb85368eed581))


### Chores

* **examples:** update honcho package versions to latest ([331ce69](https://github.com/plastic-labs/honcho-python/commit/331ce69e0400690885a9cc62d92a9403e4e3953b))

## 0.0.11 (2024-05-23)

Full Changelog: [v0.0.10...v0.0.11](https://github.com/plastic-labs/honcho-python/compare/v0.0.10...v0.0.11)

### Features

* **api:** update via SDK Studio ([#19](https://github.com/plastic-labs/honcho-python/issues/19)) ([f9c3c3e](https://github.com/plastic-labs/honcho-python/commit/f9c3c3ec4934309b402f45dbeffb21e9b564dab1))


### Chores

* **internal:** version bump ([#16](https://github.com/plastic-labs/honcho-python/issues/16)) ([e873340](https://github.com/plastic-labs/honcho-python/commit/e873340f281f09c774b6cafe1502d2b7a205bcd0))

## 0.0.10 (2024-05-23)

Full Changelog: [v0.0.9...v0.0.10](https://github.com/plastic-labs/honcho-python/compare/v0.0.9...v0.0.10)

### Features

* Release 0.0.10 Demos and LangChain Integration ([#15](https://github.com/plastic-labs/honcho-python/issues/15)) ([1c6f477](https://github.com/plastic-labs/honcho-python/commit/1c6f47742494440a6b820e416aefd105e7b1a3ec))


### Chores

* **internal:** version bump ([#13](https://github.com/plastic-labs/honcho-python/issues/13)) ([05a39a1](https://github.com/plastic-labs/honcho-python/commit/05a39a1e3796f7efcc0fd143d6b72478255b88e8))

## 0.0.9 (2024-05-23)

Full Changelog: [v0.0.8...v0.0.9](https://github.com/plastic-labs/honcho-python/compare/v0.0.8...v0.0.9)

### Features

* **api:** OpenAPI spec update via Stainless API ([#12](https://github.com/plastic-labs/honcho-python/issues/12)) ([fc9f943](https://github.com/plastic-labs/honcho-python/commit/fc9f943458b81fc897d9643ff3956ed2a859a4e9))
* **api:** update via SDK Studio ([#11](https://github.com/plastic-labs/honcho-python/issues/11)) ([08b81ed](https://github.com/plastic-labs/honcho-python/commit/08b81edd9a63e10f55575ddd3d7ca542f271aed7))


### Chores

* **internal:** version bump ([#8](https://github.com/plastic-labs/honcho-python/issues/8)) ([dac6964](https://github.com/plastic-labs/honcho-python/commit/dac6964e461965e4b111a77b22a508eac849590c))

## 0.0.8 (2024-05-16)

Full Changelog: [v0.0.8-alpha.1...v0.0.8](https://github.com/plastic-labs/honcho-python/compare/v0.0.8-alpha.1...v0.0.8)

### Features

* **api:** update via SDK Studio ([#4](https://github.com/plastic-labs/honcho-python/issues/4)) ([c8a8dbc](https://github.com/plastic-labs/honcho-python/commit/c8a8dbcf788c346ee2427762669974eb072027f0))
* **api:** update via SDK Studio ([#6](https://github.com/plastic-labs/honcho-python/issues/6)) ([5f224f6](https://github.com/plastic-labs/honcho-python/commit/5f224f611904a055860184f1d83628316ae3cf30))
* **api:** update via SDK Studio ([#7](https://github.com/plastic-labs/honcho-python/issues/7)) ([9488493](https://github.com/plastic-labs/honcho-python/commit/948849360d12d434196372b5614467ee6daf1860))

## 0.0.8-alpha.1 (2024-05-09)

Full Changelog: [v0.0.1-alpha.0...v0.0.8-alpha.1](https://github.com/plastic-labs/honcho-python/compare/v0.0.1-alpha.0...v0.0.8-alpha.1)

### Features

* **api:** OpenAPI spec update via Stainless API ([#3](https://github.com/plastic-labs/honcho-python/issues/3)) ([d2135c7](https://github.com/plastic-labs/honcho-python/commit/d2135c739d1d52b3074168d1561d85a7919663e8))
* **api:** update via SDK Studio ([c9fc257](https://github.com/plastic-labs/honcho-python/commit/c9fc2575153140bb803a0f7e674cdbcb762e9c09))
* **api:** update via SDK Studio ([c4ebb87](https://github.com/plastic-labs/honcho-python/commit/c4ebb87fc34205cc38d56a657510d83cad4b48ca))
* **api:** update via SDK Studio ([86bc8f2](https://github.com/plastic-labs/honcho-python/commit/86bc8f22ed1bed476ef578fc666533492fc3a67d))
* **api:** update via SDK Studio ([996611c](https://github.com/plastic-labs/honcho-python/commit/996611c6b9b3d9b0a6b019134bd7c31f222a356e))
* **api:** update via SDK Studio ([f1ccd91](https://github.com/plastic-labs/honcho-python/commit/f1ccd91fc4121df570b0053a1499ef2dddc9e443))
* **api:** update via SDK Studio ([4b10a42](https://github.com/plastic-labs/honcho-python/commit/4b10a422d65673f738c88aec36a556c79684dcbb))
* **api:** update via SDK Studio ([94ed61a](https://github.com/plastic-labs/honcho-python/commit/94ed61ad9140ba535c40b0551e526341b7c18901))
* **api:** update via SDK Studio ([a9df893](https://github.com/plastic-labs/honcho-python/commit/a9df8932941d6b7a1e6a2484c3e7965f1b079bb2))
* **api:** update via SDK Studio ([7d58d0b](https://github.com/plastic-labs/honcho-python/commit/7d58d0bf85b2f3c8fe9e2dcd73ca40ddf9ffd2fd))
* **api:** update via SDK Studio ([847d9c5](https://github.com/plastic-labs/honcho-python/commit/847d9c5c807a6f9f2ce981e183f5bd912fb3c6c2))
* **api:** update via SDK Studio ([45ac06b](https://github.com/plastic-labs/honcho-python/commit/45ac06b2216fc138ce3ba47eee5365eae4b96506))
* **api:** update via SDK Studio ([d1841cb](https://github.com/plastic-labs/honcho-python/commit/d1841cbf2e530d6e050df8aeeb0d1f1f06f464f0))
* **api:** update via SDK Studio ([f83704d](https://github.com/plastic-labs/honcho-python/commit/f83704dddc74d791cfdb0a26f8b17d21b1084c7c))
* **api:** update via SDK Studio ([a3b8929](https://github.com/plastic-labs/honcho-python/commit/a3b8929f1ea44bc81e9b951fd64561f3b87ee43e))
* **api:** update via SDK Studio ([b4e8264](https://github.com/plastic-labs/honcho-python/commit/b4e8264dc8217501e7156add80d3fd851a765823))
* **api:** update via SDK Studio ([00312fa](https://github.com/plastic-labs/honcho-python/commit/00312fa88bd297f45b34b78a06d7831b9fb8c91a))
* **api:** update via SDK Studio ([c3e1dbf](https://github.com/plastic-labs/honcho-python/commit/c3e1dbf8bb4d08c78ba614d2213f4e5a94ed368a))


### Chores

* go live ([#1](https://github.com/plastic-labs/honcho-python/issues/1)) ([accf7c0](https://github.com/plastic-labs/honcho-python/commit/accf7c008b22880202d49dde642444b95b362331))
