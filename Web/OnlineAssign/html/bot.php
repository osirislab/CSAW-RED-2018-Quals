<?php

function bot_impersonate($user, $path, $timeout=10) {
    $url = "http://localhost/bot_login.php?uid=" . $user->id . "&redir=" . urlencode($path);

    $cmd = array(
        "/usr/bin/timeout",
        escapeshellarg(strval($timeout)),
        "/usr/bin/chromium-browser",
        "--disable-gpu",
        "--headless",
        "--dump-dom",
        "--",
        escapeshellarg($url),
    );

    exec(implode(' ', $cmd));
}
