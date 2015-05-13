import subprocess


def run_subprocess(process):
    pr = subprocess.Popen(process, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, error) = pr.communicate()

    if error:
        print error
    else:
        print out

    return out, error