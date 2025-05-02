def user_directory_path(instance, filename):
    return 'users_{0}/{1}'.format(instance.user.id, filename)
