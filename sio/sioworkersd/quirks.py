
def apply_quirks(environ):
    # If somebody already set this, they probably know better
    if 'exclusive' not in environ:
        job = environ['job_type']
        if job == 'exec' or job == 'cpu-exec':
            environ['exclusive'] = False
        else:
            environ['exclusive'] = False
