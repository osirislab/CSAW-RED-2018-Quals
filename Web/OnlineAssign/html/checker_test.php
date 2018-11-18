<?php
require_once 'auth.php';

$u = get_user();

if (!isset($_REQUEST['qid'])) {
    die("Missing question id");
}

if (!isset($_REQUEST['aid'])) {
    die("Missing assignment id");
}

$question = Question::withID($_REQUEST['qid']);
$assignment = Assignment::withID($_REQUEST['aid']);

if ($question === null || $assignment === null) {
    http_response_code(404);
    die();
}

if ($assignment->course()->instructor()->id !== $u->id) {
    http_response_code(403);
    die();
}

$result = null;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!isset($_POST['checker'])) {
        die("Checker code must be passed");
    }

    $checker = $_POST['checker'];
    $banned_functions = array(
        "exec",
        "system",
        "passthru",
        "proc_open",
        "popen",
        "shell_exec",
        "pcntl_exec",
        "eval",
        "assert",
        "file_get_contents",
        "readfile",
    );

    foreach ($banned_functions as $badfn) {
        if (stristr($checker, $badfn) !== false) {
            die("Can't use unsafe function " . $badfn);
        }
    }

    if (isset($_POST['test_answer'])) {
        $answer = $_POST['test_answer'];
    } else {
        $answer = "";
    }

    $result = eval($checker);
}

include 'header.php';
?>
        <div class="content">
            <div>
                <h3><?php echo $question->name; ?></h3>
            </div>

            <div class="panel">
                <form action="checker_test.php" method="POST">
                    <input type="hidden" name="qid" value="<?php echo $question->id; ?>" />
                    <input type="hidden" name="aid" value="<?php echo $assignment->id; ?>" />
                    Test Answer: <input type="text" name="test_answer" /><br/>

                    <p>Checker: </p>
                    <textarea name="checker" rows="5" cols="50"><?php echo $question->checker; ?></textarea><br/>
                    <br/>

                    <?php if ($result !== null) { ?>
                    <p>Result: <?php echo $result ? "Correct" : "Incorrect"; ?></p>
                    <?php } ?>

                    <input type="submit" value="Test" />
                </form>
            </div>
        </div>
<?php
include 'footer.php';
?>
