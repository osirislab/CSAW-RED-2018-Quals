<?php
require_once 'auth.php';
require_once 'bot.php';

$u = get_user();

if (!isset($_GET['id'])) {
    die("Must set param id");
}

$msg = Message::withID($_GET['id']);

if ($msg === null) {
    http_response_code(404);
    die();
}

if ($msg->assignment()->course()->instructor()->id !== $u->id) {
    http_response_code(403);
    die();
}

include 'header.php';
?>
        <div class="content">
            <h3>Question from <?php echo $msg->student()->realname; ?> about <?php echo $msg->question()->name; ?></h3>
            <p><?php echo $msg->message; ?></p>
        </div>
<?php
include 'footer.php';
?>
