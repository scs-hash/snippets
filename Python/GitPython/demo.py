import git
from pprint import pprint

repo_path = "/Users/lavall/Onepiece/op_site"

repo = git.Repo(repo_path)

# get all branches
branches = [branch.name for branch in repo.branches]
# default branch: master / main
default_branches = "master"
commits_id = [commit.hexsha for commit in repo.iter_commits(default_branches)]
pprint(branches)
# ['master']
pprint(commits_id)

#['55dafb7f70e9ef2a7dd94e0eccee20191690f4e7',
# '193ace696e184aa10885c2a62e2e5fe7b06c32b4',
# 'c3ebd61841a10da3b4d84457af4ca6deffbc3d97',
# 'be2a32a279f3a65ad2a51a111630db68da673771',
# '26d1e0ae1360891e635c17089a980f80f1f38359',
# '2099ea5f42d82ba41208c9e293ddbb4dfa2ff028',
# '515659e4a49b67f9cd8a127907c2997f027b5c85',
# '0dd26a0ca24ad879ef2ee129c78d0e980b417679',
# 'de5fe27049f8331476fac84ecbefcafb6e5b12ab',
# 'ff5925131b08455aab77726e13cc566e6fce4041',
# '3e8c99da411cc7bb385a235a21c42397e197f02d',
# 'e70008c92a340e32985a15bd655e5a4753a7c21a',
# 'd442fc236dd57c05376aabe4381751bc8e0f92d5',
# '71ff4d49aebf189c5975d69f973d10bebf3e81a6',
# '3647d8c28f9c183b6071fc253299fadea1f75653',
# '1eb96dab4cf13246bac6bd792d1a52130d44892a',
# '32faf0ee6a4541d8d900a46cd0ec047f54c5b8c5',
# '713056bd4591f4b27935830d72d9f391ef277a03',
# '84e79acba7fae2cea96d302ab4006e911c59a9c4',
# 'cef5a7bd548a960ed94cfb01df15bdaf633b43af',
# 'f3a697e01ec0c6592937de31dd4b18bf84d84aa2',
# 'd5df96f79a4958dea37f4eb729feab33f4a54b7e',
# '31c0694a5d143ca5677dc6c353bcdc34734ab77e',
# 'a7a3fe3ba58d601aba831f983aaeef05bb1d0496',
# '8fc7ba88a8961e55e69b11a8af142ceeaedf3638',
# '10c05c521507cc99b1f22ddf534f4d0f8ec32422',
# '69365ebef2c38dbd8eca8fe427739df217f93ec2',
# '9934f2844f208d441b873096150133f5c30a7cef',
# '1dedda12904ff1750dbd2dd1168979741ffdbdad',
# '7d33ec1b3531a87ccc18317df287dcee8a55dbe7',
# 'e946df9f26ffb2058cdb3bda29100b4ddcf14f31',
# '8ef7fdb7b5ccece5e7b5e84b44dec267969df2ba',
# 'e99c6782f53c93c705f31c21bdd257f328373202',
# '7cf70b82c3eb79facf2d401b87e504afe9076032',
# '21616d9593b816d44b6df3d436fb5678da84d01f',
# '94e6952f6c8604a35b159d2583d3fb6e43e2ec34',
# '73b7586a5933d9860013a37456c6e973a9f5008b',
# '07b888eaff183cdaa0bef1e248973e7d2e7c9c90',
# '0bbdf58901cb1f437e4be39e1bee7eb5f2b4fa19',
# 'c90e9c2de6732b891a5a42759116fc5ba63bf6bd',
# 'ea78eeea068d23d8660c74da599d431002afa9d5',
# '24158179ab64b5838811544bd90415bdef744563',
# '00170827d3d7618320f20cdb136dfdcc12502f5d',
# '7e58ea4e2d892e9ec86693a8c1b761f631cf3034',
# 'c347f7a2fb30cd56b1ae23cb8eeab33362eec822',
# 'd07fd93353334ce9d8733f5d47227e53ed359f0e',
# '5ac170fb5a8f6545cde85d3652ee1364bc0f09ab',
# '709c33074486d19106cc58165d83baeb9a6323c9',
# '494f8e5cee6fca8d089a7e672332bb4911aa0052',
# '03f42d9a1e5a5d921a1d4253f126a1faa37155c5',
# 'db45e684bad2d65605c1ead6441f228bd6a9bc2f',
# 'a35c6c4b377f7ea3db5933d61b98928fea9cd665',
# '390132763d538c771e43d13c1bf3c63088ad655f',
# 'a402331c13f2a9517816bf22ee327bff95afa04a',
# 'd667648ff1cf370c37eb6c7ce6b67773d75bcac1',
# 'b2550896fae86505fa5359d3e00354d8055ba9bf',
# 'b0ac53079979af57e1718eb1ff19474aa2a96934',
# '7eb91c6d74b71cdcb2f1dc6c18b7fcfe2582e2c0',
# '7700e46e1d761bbaf446af017f7f410e87f5bebe',
# '99e5500ef3126e3f872fbeb9efdf53f017073f5d',
# '247dc4afbfbb512cfdee3ccb7356125006dba7cd',
# 'ef1b434b31ea29a02ac38d8e8df7813a03ccb6a3',
# '10bf04252eae15aded71621073e0634e0ea7b891',
# '596d38c2957e5542dd210a82c4454c8430d6e8e0',
# '953859736e37e90f4f83d213f288fe0c48c56f96',
# 'ca8c267b04901b6f0d3d01963e34cc7dd4b63c8d',
# 'cdd66820ecb52385249b31434946e828906d1e57',
# '989aae99ab188395ad6595c9689606a8c46692f3',
# 'd2a81342d02fe312dc4a924d2130b73df86cf44f',
# '8c91600d75b5d9a0a80e0b069a11b0b142e51690',
# 'c6980a5960cd6cff9efdd8db704fcc77183191bc',
# '0a202834145c038a42b912673bf09bb67d4b583c',
# '774053a6684520cf92bc5746533338628d906c79',
# '07917341d32a760f55d56a5a42f9642383fe37d6',
# 'd37e20c558f6fac1757a84aead7c1f43bb576d4e',
# 'ce9b166f30461cf3324e998f8a97f74033a403e1',
# 'c343b57740758184159b66fb5bae008dae5b8734',
# '6e46a3dfd0087c25e8da986313347567fc98146d',
# '5fbeb74b826cad5317353cce1c44049c13b2555c',
# 'c539a97e185951f066b9415ef90af2907ffa50db',
# '8f7ef28020fe0fd8c2d1dc70a62ac4a7f3b9737a',
# 'f2be294f952ea9f5944c044bbf88b98d0d4651b7',
# 'dcd3fb5999b00ddcca9b57cda9093756fdaebdb3',
# '14faf7597066d4db8b581f3ad90839dfc01369a1',
# 'a497a916a28cfe62255e43eb9a491637a41824b8',
# '2d4b23ff651222e827f165954adc97c116ef37f2',
# '6c539b412011dc4f13fd980b127cf27dd64c0c1e',
# '32ab4459bbfb7789733951ecb818e597b39c2dca',
# '7de52140e4b0608f64716481dc98160ab69f2e8b',
# '313e398e3167cfd1913c9828c18231cf02f75628',
# '1127c950ff9377ebfae0f74cc727fa8c969b2a65',
# '9b5ae25175552e96f7f9f4a192ed8ebaa94bf9b7',
# 'f1150252a237af8c55f1e459448b00d1a0968e9e',
# 'fc09a78759551d9a6b1c2c90b5db274a25a10cfb',
# 'e311c4f5338ddc2e811b7d795ef0013285b95cdb',
# '020f5f66cd592187db6f8742dc72edfe78d0932d',
# 'b884c2e55654186ad0b4c39c3efbb561c310ad5b',
# 'bfc78b3b9fbd673d60f33580be910fae507cd134',
# '313f70ddcaec9790d0d014b036cbc329a4df68c3',
# '8d0b82418ec09e53d041e0907449a098040e716f',
# '84c5b6a0643d4e44ab03348a1e8c59c2de017d41',
# 'c46cfeb180b3efea60d4713c7bce18b20203d2af',
# '86f66d75683a64b19adc9a79a3594683a176f673',
# 'ae60de5871a196dc831d5bff7bae45f6cf2686fe',
# 'a8a751acef949250b6f38ffd034b24859b24b0af',
# '92926fa80e787a901c3299fd6c9178cc12d89e8e',
# '85a962ccd7ab582f95b01db76dc4d03e9a7c43ec',
# '5222d5b0546899a866591bd42d44d252901f1764',
# '0a26ccde8eac110b90b5908329bd3f9bc7f2c35d',
# 'd691fc024bcc3a04ec7308d727ee5dc3fb99e02d',
# '788373dcd337cc49daac2d63050be4d75f31429c',
# '1d457a46961fe2755ebc7c0b158af30eac27b9be',
# 'e36b3167bc48060d17380301570fb5b9a2811e77',
# '81729c2dc394351b5b4c5c4a29259eb8ee1041ad',
# '485e1542c3bb36a3179808be61887431053099bc',
# '1ee8893d3d684d59b1e197e8374b422d72bd769e',
# '72cc1b66f8adc82c4ad80f6238f28a838666cf05',
# 'dea81e76d12caad4720a173f13d740dd6e5300b0',
# '1ad0e753d9f987e0b3368334b54ef469a2e20fa7',
# '26d581c71be172d1ef88399e5082b3b1cb04dd12',
# 'e0a00c9c6ca96168567bef726153a6e0df9983e9',
# '872e106d133948a029045c6bf24163ac0a309aad',
# '84d19b945d5c760b16e24669f1152abe8db067af',
# 'a81e6cc5c991c1777f58ca54ff4a15e6f2f17cf2',
# '3a74ab0507dff41315f3eaec1432e0b3974a5b32',
# 'af88c546de252f7d358ee306ab6cfbf3503d95a7',
# '6ce6f1f578c2f00874e82a6d19755a216120d3a0',
# 'b3a8fbfe7d5587def0c524fd84b3033ae49b4e0f',
# '4d7bcd7d46e94966180c7a5dbd6b64de3687507c',
# '3d7edb93d7597b65d4045ce92044fb83dbc5de00',
# '9d95e6d365a641d7bc1701a93d675164196e47af',
# '38b5d2d709c58916d5d4f14d29940dadb46c67d4',
# '4282815c9317e22bb241be1d15fbf12ca668831f',
# '3c6cdd5dc8b7a7ed86051d662d6e9685179b5146',
# 'aa7be5aed5716bc0e09bef6d4db4e01f6dacc008',
# '3047aa54c3561b18dc08fbc5b1018a906f251741',
# '68d5c0fb3a5886fc3880edeb9355a47baf834d8d',
# 'a76c6ded8a2c8f9d952dcce1ce3c662d67c3de99',
# '9455728259ed337533e1c7fb0621873d032073fc',
# '05f87ba950dc9200bdd51d3a0b51c714f64b6291']