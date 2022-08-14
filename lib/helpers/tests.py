# Copied from https://qna.habr.com/q/632914.


from io import StringIO
import sys


class OutputInterceptor(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout


with OutputInterceptor() as output:
    # Любой вывод в консоль из этого блока будет сохраняться в переменную output
    print('123')


print('\n'.join(output))
