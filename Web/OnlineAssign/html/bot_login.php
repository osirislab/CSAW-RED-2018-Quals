<?php

if (!($_SERVER['REMOTE_ADDR'] === '127.0.0.1' || $_SERVER['REMOTE_ADDR'] === '::1')) {
    header('HTTP/1.1 403 Forbidden');
    die();
}

require_once 'auth.php';
require_once 'models.php';

set_user(User::withID($_GET['uid']));

header('Location: ' . $_GET['redir']);
