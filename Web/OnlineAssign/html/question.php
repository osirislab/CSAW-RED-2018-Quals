<?php
require_once 'auth.php';
require_once 'bot.php';

$u = get_user();

if (!isset($_REQUEST['aid'])) {
    die("Missing assignment id");
}

if (!isset($_REQUEST['qid'])) {
    die("Missing question id");
}

$a = Assignment::withID($_REQUEST['aid']);
$q = Question::withID($_REQUEST['qid']);

if ($a === null || $q === null) {
    http_response_code(404);
    die();
}

$error = null;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!isset($_POST['message'])) {
        $error = "You must have a message";
    }

    if ($error === null) {
        $message = $_POST['message'];
        $instructor = $a->course()->instructor();
        $msg_id = Message::send($u, $instructor, $q, $a, $message);
        bot_impersonate($instructor, "instructor_answer.php?id=" . $msg_id);
    }
}

include 'header.php';
?>
        <div class="content">
            <h3>Ask a question</h3>
<?php if ($error !== null) { ?>
            <p class="error"><?php echo $error; ?></p>
<?php } ?>
            <div class="panel">
                <h5><?php echo $q->name; ?></h5>
                <p><?php echo $q->body; ?></p>
            </div>
            <div class="panel">
                <form action="question.php" method="POST">
                    <input type="hidden" name="aid" value="<?php echo $a->id; ?>" />
                    <input type="hidden" name="qid" value="<?php echo $q->id; ?>" />
                    <textarea name="message" rows="5" cols="50">Question for your teacher</textarea><br/>
                    <br/>
                    <input type="submit" value="Submit" />
                </form>
            </div>
        </div>
<?php
include 'footer.php';
?>
