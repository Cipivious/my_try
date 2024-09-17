from tempfile import TemporaryFile

f = TemporaryFile()
f.write("b" * 1024 * 1024)
f.close()