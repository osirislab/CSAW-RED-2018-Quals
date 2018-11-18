<?php

session_start();

function require_login() {
    if (!isset($_SESSION['uid'])) {
        header('Location: login.php');
        die();
    }
}

function get_user() {
    require_login();

    require_once 'models.php';
    
    return User::withID($_SESSION['uid']);
}

function set_user($u) {
    $_SESSION['uid'] = $u->id;
}
