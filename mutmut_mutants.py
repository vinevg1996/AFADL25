
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


def x_run__mutmut_orig(self, play):
    if not self._callbacks_loaded:
        self.load_callbacks()

    all_vars = self._variable_manager.get_vars(play=play)
    templar = Templar(loader=self._loader, variables=all_vars)

    new_play = play.copy()
    new_play.post_validate(templar)
    new_play.handlers = new_play.compile_roles_handlers() + new_play.handlers

    self.hostvars = HostVars(
        inventory=self._inventory,
        variable_manager=self._variable_manager,
        loader=self._loader,
    )

    play_context = PlayContext(new_play, self.passwords, self._connection_lockfile.fileno())
    if (self._stdout_callback and
            hasattr(self._stdout_callback, 'set_play_context')):
        self._stdout_callback.set_play_context(play_context)

    for callback_plugin in self._callback_plugins:
        if hasattr(callback_plugin, 'set_play_context'):
            callback_plugin.set_play_context(play_context)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
def x_run__mutmut_1(self, play):
    if  self._callbacks_loaded:
        self.load_callbacks()

    all_vars = self._variable_manager.get_vars(play=play)
    templar = Templar(loader=self._loader, variables=all_vars)

    new_play = play.copy()
    new_play.post_validate(templar)
    new_play.handlers = new_play.compile_roles_handlers() + new_play.handlers

    self.hostvars = HostVars(
        inventory=self._inventory,
        variable_manager=self._variable_manager,
        loader=self._loader,
    )

    play_context = PlayContext(new_play, self.passwords, self._connection_lockfile.fileno())
    if (self._stdout_callback and
            hasattr(self._stdout_callback, 'set_play_context')):
        self._stdout_callback.set_play_context(play_context)

    for callback_plugin in self._callback_plugins:
        if hasattr(callback_plugin, 'set_play_context'):
            callback_plugin.set_play_context(play_context)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
def x_run__mutmut_2(self, play):
    if not self._callbacks_loaded:
        self.load_callbacks()

    all_vars = self._variable_manager.get_vars(play=None)
    templar = Templar(loader=self._loader, variables=all_vars)

    new_play = play.copy()
    new_play.post_validate(templar)
    new_play.handlers = new_play.compile_roles_handlers() + new_play.handlers

    self.hostvars = HostVars(
        inventory=self._inventory,
        variable_manager=self._variable_manager,
        loader=self._loader,
    )

    play_context = PlayContext(new_play, self.passwords, self._connection_lockfile.fileno())
    if (self._stdout_callback and
            hasattr(self._stdout_callback, 'set_play_context')):
        self._stdout_callback.set_play_context(play_context)

    for callback_plugin in self._callback_plugins:
        if hasattr(callback_plugin, 'set_play_context'):
            callback_plugin.set_play_context(play_context)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
def x_run__mutmut_3(self, play):
    if not self._callbacks_loaded:
        self.load_callbacks()

    all_vars = None
    templar = Templar(loader=self._loader, variables=all_vars)

    new_play = play.copy()
    new_play.post_validate(templar)
    new_play.handlers = new_play.compile_roles_handlers() + new_play.handlers

    self.hostvars = HostVars(
        inventory=self._inventory,
        variable_manager=self._variable_manager,
        loader=self._loader,
    )

    play_context = PlayContext(new_play, self.passwords, self._connection_lockfile.fileno())
    if (self._stdout_callback and
            hasattr(self._stdout_callback, 'set_play_context')):
        self._stdout_callback.set_play_context(play_context)

    for callback_plugin in self._callback_plugins:
        if hasattr(callback_plugin, 'set_play_context'):
            callback_plugin.set_play_context(play_context)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
def x_run__mutmut_4(self, play):
    if not self._callbacks_loaded:
        self.load_callbacks()

    all_vars = self._variable_manager.get_vars(play=play)
    templar = Templar(loader=self._loader, variables=None)

    new_play = play.copy()
    new_play.post_validate(templar)
    new_play.handlers = new_play.compile_roles_handlers() + new_play.handlers

    self.hostvars = HostVars(
        inventory=self._inventory,
        variable_manager=self._variable_manager,
        loader=self._loader,
    )

    play_context = PlayContext(new_play, self.passwords, self._connection_lockfile.fileno())
    if (self._stdout_callback and
            hasattr(self._stdout_callback, 'set_play_context')):
        self._stdout_callback.set_play_context(play_context)

    for callback_plugin in self._callback_plugins:
        if hasattr(callback_plugin, 'set_play_context'):
            callback_plugin.set_play_context(play_context)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
def x_run__mutmut_5(self, play):
    if not self._callbacks_loaded:
        self.load_callbacks()

    all_vars = self._variable_manager.get_vars(play=play)
    templar = Templar( variables=all_vars)

    new_play = play.copy()
    new_play.post_validate(templar)
    new_play.handlers = new_play.compile_roles_handlers() + new_play.handlers

    self.hostvars = HostVars(
        inventory=self._inventory,
        variable_manager=self._variable_manager,
        loader=self._loader,
    )

    play_context = PlayContext(new_play, self.passwords, self._connection_lockfile.fileno())
    if (self._stdout_callback and
            hasattr(self._stdout_callback, 'set_play_context')):
        self._stdout_callback.set_play_context(play_context)

    for callback_plugin in self._callback_plugins:
        if hasattr(callback_plugin, 'set_play_context'):
            callback_plugin.set_play_context(play_context)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
def x_run__mutmut_6(self, play):
    if not self._callbacks_loaded:
        self.load_callbacks()

    all_vars = self._variable_manager.get_vars(play=play)
    templar = Templar(loader=self._loader,)

    new_play = play.copy()
    new_play.post_validate(templar)
    new_play.handlers = new_play.compile_roles_handlers() + new_play.handlers

    self.hostvars = HostVars(
        inventory=self._inventory,
        variable_manager=self._variable_manager,
        loader=self._loader,
    )

    play_context = PlayContext(new_play, self.passwords, self._connection_lockfile.fileno())
    if (self._stdout_callback and
            hasattr(self._stdout_callback, 'set_play_context')):
        self._stdout_callback.set_play_context(play_context)

    for callback_plugin in self._callback_plugins:
        if hasattr(callback_plugin, 'set_play_context'):
            callback_plugin.set_play_context(play_context)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
def x_run__mutmut_7(self, play):
    if not self._callbacks_loaded:
        self.load_callbacks()

    all_vars = self._variable_manager.get_vars(play=play)
    templar = None

    new_play = play.copy()
    new_play.post_validate(templar)
    new_play.handlers = new_play.compile_roles_handlers() + new_play.handlers

    self.hostvars = HostVars(
        inventory=self._inventory,
        variable_manager=self._variable_manager,
        loader=self._loader,
    )

    play_context = PlayContext(new_play, self.passwords, self._connection_lockfile.fileno())
    if (self._stdout_callback and
            hasattr(self._stdout_callback, 'set_play_context')):
        self._stdout_callback.set_play_context(play_context)

    for callback_plugin in self._callback_plugins:
        if hasattr(callback_plugin, 'set_play_context'):
            callback_plugin.set_play_context(play_context)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
def x_run__mutmut_8(self, play):
    if not self._callbacks_loaded:
        self.load_callbacks()

    all_vars = self._variable_manager.get_vars(play=play)
    templar = Templar(loader=self._loader, variables=all_vars)

    new_play = None
    new_play.post_validate(templar)
    new_play.handlers = new_play.compile_roles_handlers() + new_play.handlers

    self.hostvars = HostVars(
        inventory=self._inventory,
        variable_manager=self._variable_manager,
        loader=self._loader,
    )

    play_context = PlayContext(new_play, self.passwords, self._connection_lockfile.fileno())
    if (self._stdout_callback and
            hasattr(self._stdout_callback, 'set_play_context')):
        self._stdout_callback.set_play_context(play_context)

    for callback_plugin in self._callback_plugins:
        if hasattr(callback_plugin, 'set_play_context'):
            callback_plugin.set_play_context(play_context)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
def x_run__mutmut_9(self, play):
    if not self._callbacks_loaded:
        self.load_callbacks()

    all_vars = self._variable_manager.get_vars(play=play)
    templar = Templar(loader=self._loader, variables=all_vars)

    new_play = play.copy()
    new_play.post_validate(None)
    new_play.handlers = new_play.compile_roles_handlers() + new_play.handlers

    self.hostvars = HostVars(
        inventory=self._inventory,
        variable_manager=self._variable_manager,
        loader=self._loader,
    )

    play_context = PlayContext(new_play, self.passwords, self._connection_lockfile.fileno())
    if (self._stdout_callback and
            hasattr(self._stdout_callback, 'set_play_context')):
        self._stdout_callback.set_play_context(play_context)

    for callback_plugin in self._callback_plugins:
        if hasattr(callback_plugin, 'set_play_context'):
            callback_plugin.set_play_context(play_context)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
def x_run__mutmut_10(self, play):
    if not self._callbacks_loaded:
        self.load_callbacks()

    all_vars = self._variable_manager.get_vars(play=play)
    templar = Templar(loader=self._loader, variables=all_vars)

    new_play = play.copy()
    new_play.post_validate(templar)
    new_play.handlers = new_play.compile_roles_handlers() - new_play.handlers

    self.hostvars = HostVars(
        inventory=self._inventory,
        variable_manager=self._variable_manager,
        loader=self._loader,
    )

    play_context = PlayContext(new_play, self.passwords, self._connection_lockfile.fileno())
    if (self._stdout_callback and
            hasattr(self._stdout_callback, 'set_play_context')):
        self._stdout_callback.set_play_context(play_context)

    for callback_plugin in self._callback_plugins:
        if hasattr(callback_plugin, 'set_play_context'):
            callback_plugin.set_play_context(play_context)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
def x_run__mutmut_11(self, play):
    if not self._callbacks_loaded:
        self.load_callbacks()

    all_vars = self._variable_manager.get_vars(play=play)
    templar = Templar(loader=self._loader, variables=all_vars)

    new_play = play.copy()
    new_play.post_validate(templar)
    new_play.handlers = None

    self.hostvars = HostVars(
        inventory=self._inventory,
        variable_manager=self._variable_manager,
        loader=self._loader,
    )

    play_context = PlayContext(new_play, self.passwords, self._connection_lockfile.fileno())
    if (self._stdout_callback and
            hasattr(self._stdout_callback, 'set_play_context')):
        self._stdout_callback.set_play_context(play_context)

    for callback_plugin in self._callback_plugins:
        if hasattr(callback_plugin, 'set_play_context'):
            callback_plugin.set_play_context(play_context)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
def x_run__mutmut_12(self, play):
    if not self._callbacks_loaded:
        self.load_callbacks()

    all_vars = self._variable_manager.get_vars(play=play)
    templar = Templar(loader=self._loader, variables=all_vars)

    new_play = play.copy()
    new_play.post_validate(templar)
    new_play.handlers = new_play.compile_roles_handlers() + new_play.handlers

    self.hostvars = HostVars(
        variable_manager=self._variable_manager,
        loader=self._loader,
    )

    play_context = PlayContext(new_play, self.passwords, self._connection_lockfile.fileno())
    if (self._stdout_callback and
            hasattr(self._stdout_callback, 'set_play_context')):
        self._stdout_callback.set_play_context(play_context)

    for callback_plugin in self._callback_plugins:
        if hasattr(callback_plugin, 'set_play_context'):
            callback_plugin.set_play_context(play_context)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
def x_run__mutmut_13(self, play):
    if not self._callbacks_loaded:
        self.load_callbacks()

    all_vars = self._variable_manager.get_vars(play=play)
    templar = Templar(loader=self._loader, variables=all_vars)

    new_play = play.copy()
    new_play.post_validate(templar)
    new_play.handlers = new_play.compile_roles_handlers() + new_play.handlers

    self.hostvars = HostVars(
        inventory=self._inventory,
        loader=self._loader,
    )

    play_context = PlayContext(new_play, self.passwords, self._connection_lockfile.fileno())
    if (self._stdout_callback and
            hasattr(self._stdout_callback, 'set_play_context')):
        self._stdout_callback.set_play_context(play_context)

    for callback_plugin in self._callback_plugins:
        if hasattr(callback_plugin, 'set_play_context'):
            callback_plugin.set_play_context(play_context)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
def x_run__mutmut_14(self, play):
    if not self._callbacks_loaded:
        self.load_callbacks()

    all_vars = self._variable_manager.get_vars(play=play)
    templar = Templar(loader=self._loader, variables=all_vars)

    new_play = play.copy()
    new_play.post_validate(templar)
    new_play.handlers = new_play.compile_roles_handlers() + new_play.handlers

    self.hostvars = HostVars(
        inventory=self._inventory,
        variable_manager=self._variable_manager,
    )

    play_context = PlayContext(new_play, self.passwords, self._connection_lockfile.fileno())
    if (self._stdout_callback and
            hasattr(self._stdout_callback, 'set_play_context')):
        self._stdout_callback.set_play_context(play_context)

    for callback_plugin in self._callback_plugins:
        if hasattr(callback_plugin, 'set_play_context'):
            callback_plugin.set_play_context(play_context)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
def x_run__mutmut_15(self, play):
    if not self._callbacks_loaded:
        self.load_callbacks()

    all_vars = self._variable_manager.get_vars(play=play)
    templar = Templar(loader=self._loader, variables=all_vars)

    new_play = play.copy()
    new_play.post_validate(templar)
    new_play.handlers = new_play.compile_roles_handlers() + new_play.handlers

    self.hostvars = None

    play_context = PlayContext(new_play, self.passwords, self._connection_lockfile.fileno())
    if (self._stdout_callback and
            hasattr(self._stdout_callback, 'set_play_context')):
        self._stdout_callback.set_play_context(play_context)

    for callback_plugin in self._callback_plugins:
        if hasattr(callback_plugin, 'set_play_context'):
            callback_plugin.set_play_context(play_context)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
def x_run__mutmut_16(self, play):
    if not self._callbacks_loaded:
        self.load_callbacks()

    all_vars = self._variable_manager.get_vars(play=play)
    templar = Templar(loader=self._loader, variables=all_vars)

    new_play = play.copy()
    new_play.post_validate(templar)
    new_play.handlers = new_play.compile_roles_handlers() + new_play.handlers

    self.hostvars = HostVars(
        inventory=self._inventory,
        variable_manager=self._variable_manager,
        loader=self._loader,
    )

    play_context = PlayContext(None, self.passwords, self._connection_lockfile.fileno())
    if (self._stdout_callback and
            hasattr(self._stdout_callback, 'set_play_context')):
        self._stdout_callback.set_play_context(play_context)

    for callback_plugin in self._callback_plugins:
        if hasattr(callback_plugin, 'set_play_context'):
            callback_plugin.set_play_context(play_context)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
def x_run__mutmut_17(self, play):
    if not self._callbacks_loaded:
        self.load_callbacks()

    all_vars = self._variable_manager.get_vars(play=play)
    templar = Templar(loader=self._loader, variables=all_vars)

    new_play = play.copy()
    new_play.post_validate(templar)
    new_play.handlers = new_play.compile_roles_handlers() + new_play.handlers

    self.hostvars = HostVars(
        inventory=self._inventory,
        variable_manager=self._variable_manager,
        loader=self._loader,
    )

    play_context = PlayContext( self.passwords, self._connection_lockfile.fileno())
    if (self._stdout_callback and
            hasattr(self._stdout_callback, 'set_play_context')):
        self._stdout_callback.set_play_context(play_context)

    for callback_plugin in self._callback_plugins:
        if hasattr(callback_plugin, 'set_play_context'):
            callback_plugin.set_play_context(play_context)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
def x_run__mutmut_18(self, play):
    if not self._callbacks_loaded:
        self.load_callbacks()

    all_vars = self._variable_manager.get_vars(play=play)
    templar = Templar(loader=self._loader, variables=all_vars)

    new_play = play.copy()
    new_play.post_validate(templar)
    new_play.handlers = new_play.compile_roles_handlers() + new_play.handlers

    self.hostvars = HostVars(
        inventory=self._inventory,
        variable_manager=self._variable_manager,
        loader=self._loader,
    )

    play_context = None
    if (self._stdout_callback and
            hasattr(self._stdout_callback, 'set_play_context')):
        self._stdout_callback.set_play_context(play_context)

    for callback_plugin in self._callback_plugins:
        if hasattr(callback_plugin, 'set_play_context'):
            callback_plugin.set_play_context(play_context)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
def x_run__mutmut_19(self, play):
    if not self._callbacks_loaded:
        self.load_callbacks()

    all_vars = self._variable_manager.get_vars(play=play)
    templar = Templar(loader=self._loader, variables=all_vars)

    new_play = play.copy()
    new_play.post_validate(templar)
    new_play.handlers = new_play.compile_roles_handlers() + new_play.handlers

    self.hostvars = HostVars(
        inventory=self._inventory,
        variable_manager=self._variable_manager,
        loader=self._loader,
    )

    play_context = PlayContext(new_play, self.passwords, self._connection_lockfile.fileno())
    if (self._stdout_callback and
            hasattr(self._stdout_callback, 'XXset_play_contextXX')):
        self._stdout_callback.set_play_context(play_context)

    for callback_plugin in self._callback_plugins:
        if hasattr(callback_plugin, 'set_play_context'):
            callback_plugin.set_play_context(play_context)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
def x_run__mutmut_20(self, play):
    if not self._callbacks_loaded:
        self.load_callbacks()

    all_vars = self._variable_manager.get_vars(play=play)
    templar = Templar(loader=self._loader, variables=all_vars)

    new_play = play.copy()
    new_play.post_validate(templar)
    new_play.handlers = new_play.compile_roles_handlers() + new_play.handlers

    self.hostvars = HostVars(
        inventory=self._inventory,
        variable_manager=self._variable_manager,
        loader=self._loader,
    )

    play_context = PlayContext(new_play, self.passwords, self._connection_lockfile.fileno())
    if (self._stdout_callback or
            hasattr(self._stdout_callback, 'set_play_context')):
        self._stdout_callback.set_play_context(play_context)

    for callback_plugin in self._callback_plugins:
        if hasattr(callback_plugin, 'set_play_context'):
            callback_plugin.set_play_context(play_context)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
def x_run__mutmut_21(self, play):
    if not self._callbacks_loaded:
        self.load_callbacks()

    all_vars = self._variable_manager.get_vars(play=play)
    templar = Templar(loader=self._loader, variables=all_vars)

    new_play = play.copy()
    new_play.post_validate(templar)
    new_play.handlers = new_play.compile_roles_handlers() + new_play.handlers

    self.hostvars = HostVars(
        inventory=self._inventory,
        variable_manager=self._variable_manager,
        loader=self._loader,
    )

    play_context = PlayContext(new_play, self.passwords, self._connection_lockfile.fileno())
    if (self._stdout_callback and
            hasattr(self._stdout_callback, 'set_play_context')):
        self._stdout_callback.set_play_context(None)

    for callback_plugin in self._callback_plugins:
        if hasattr(callback_plugin, 'set_play_context'):
            callback_plugin.set_play_context(play_context)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
def x_run__mutmut_22(self, play):
    if not self._callbacks_loaded:
        self.load_callbacks()

    all_vars = self._variable_manager.get_vars(play=play)
    templar = Templar(loader=self._loader, variables=all_vars)

    new_play = play.copy()
    new_play.post_validate(templar)
    new_play.handlers = new_play.compile_roles_handlers() + new_play.handlers

    self.hostvars = HostVars(
        inventory=self._inventory,
        variable_manager=self._variable_manager,
        loader=self._loader,
    )

    play_context = PlayContext(new_play, self.passwords, self._connection_lockfile.fileno())
    if (self._stdout_callback and
            hasattr(self._stdout_callback, 'set_play_context')):
        self._stdout_callback.set_play_context(play_context)

    for callback_plugin in self._callback_plugins:
        if hasattr(None, 'set_play_context'):
            callback_plugin.set_play_context(play_context)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
def x_run__mutmut_23(self, play):
    if not self._callbacks_loaded:
        self.load_callbacks()

    all_vars = self._variable_manager.get_vars(play=play)
    templar = Templar(loader=self._loader, variables=all_vars)

    new_play = play.copy()
    new_play.post_validate(templar)
    new_play.handlers = new_play.compile_roles_handlers() + new_play.handlers

    self.hostvars = HostVars(
        inventory=self._inventory,
        variable_manager=self._variable_manager,
        loader=self._loader,
    )

    play_context = PlayContext(new_play, self.passwords, self._connection_lockfile.fileno())
    if (self._stdout_callback and
            hasattr(self._stdout_callback, 'set_play_context')):
        self._stdout_callback.set_play_context(play_context)

    for callback_plugin in self._callback_plugins:
        if hasattr(callback_plugin, 'XXset_play_contextXX'):
            callback_plugin.set_play_context(play_context)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
def x_run__mutmut_24(self, play):
    if not self._callbacks_loaded:
        self.load_callbacks()

    all_vars = self._variable_manager.get_vars(play=play)
    templar = Templar(loader=self._loader, variables=all_vars)

    new_play = play.copy()
    new_play.post_validate(templar)
    new_play.handlers = new_play.compile_roles_handlers() + new_play.handlers

    self.hostvars = HostVars(
        inventory=self._inventory,
        variable_manager=self._variable_manager,
        loader=self._loader,
    )

    play_context = PlayContext(new_play, self.passwords, self._connection_lockfile.fileno())
    if (self._stdout_callback and
            hasattr(self._stdout_callback, 'set_play_context')):
        self._stdout_callback.set_play_context(play_context)

    for callback_plugin in self._callback_plugins:
        if hasattr( 'set_play_context'):
            callback_plugin.set_play_context(play_context)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
def x_run__mutmut_25(self, play):
    if not self._callbacks_loaded:
        self.load_callbacks()

    all_vars = self._variable_manager.get_vars(play=play)
    templar = Templar(loader=self._loader, variables=all_vars)

    new_play = play.copy()
    new_play.post_validate(templar)
    new_play.handlers = new_play.compile_roles_handlers() + new_play.handlers

    self.hostvars = HostVars(
        inventory=self._inventory,
        variable_manager=self._variable_manager,
        loader=self._loader,
    )

    play_context = PlayContext(new_play, self.passwords, self._connection_lockfile.fileno())
    if (self._stdout_callback and
            hasattr(self._stdout_callback, 'set_play_context')):
        self._stdout_callback.set_play_context(play_context)

    for callback_plugin in self._callback_plugins:
        if hasattr(callback_plugin, 'set_play_context'):
            callback_plugin.set_play_context(None)

    self.send_callback('v2_playbook_on_play_start', new_play)

    iterator = PlayIterator(
        inventory=self._inventory,
        play=new_play,
        play_context=play_context,
        variable_manager=self._variable_manager,
        all_vars=all_vars,
        start_at_done=self._start_at_done,
    )

    self._initialize_processes(min(self._forks, iterator.batch_size))

    strategy = strategy_loader.get(new_play.strategy, self)
    if strategy is None:
        raise AnsibleError("Invalid play strategy specified: %s" % new_play.strategy, obj=play._ds)

    for host_name in self._failed_hosts.keys():
        host = self._inventory.get_host(host_name)
        iterator.mark_host_failed(host)
    for host_name in self._unreachable_hosts.keys():
        iterator._play._removed_hosts.append(host_name)

    self.clear_failed_hosts()

    if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:
        self._start_at_done = True

    try:
        play_return = strategy.run(iterator, play_context)
    finally:
        strategy.cleanup()
        self._cleanup_processes()

    for host_name in iterator.get_failed_hosts():
        self._failed_hosts[host_name] = True

    if iterator.end_play:
        raise AnsibleEndPlay(play_return)

    return play_return
