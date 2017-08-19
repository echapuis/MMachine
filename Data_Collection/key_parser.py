
def parse(file='Data_Collection/keys'):
    result = {}
    for line in open(file).readlines():
        if not line.strip(): continue
        split = line.split(':')
        assert len(split) == 2, 'Each line in key document must have format key:value'
        key, value = split[0].lower().strip(), split[1].strip()
        result[key] = value
    return result
