class Solution:
    def simplifyPath(self, path: str) -> str:
        w = ""
        path += '/'
        canonical_path = ''

        for c in path:
            if c == '/':
                if w == '.':
                    print(w)
                elif w == '..':
                    dirs = canonical_path.split('/')
                    canonical_path = '/'.join(dirs[:-2]) + '/'
                elif w != '':
                    print(w)
                    canonical_path += w + '/'

                w = ""
            else:
                w += c

        
        return '/' + canonical_path.strip('/')