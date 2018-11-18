<?php
require_once 'auth.php';

$u = get_user();

if (!isset($_REQUEST['id'])) {
    die("Missing id");
}

$assignment = Assignment::withID($_REQUEST['id']);

if ($assignment == null) {
    http_response_code(404);
    die();
}

if ($assignment->course()->instructor()->id !== $u->id) {
    http_response_code(403);
    die();
}

$error = null;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $error = "Database offline in scheduled maintenance. Try again after Oct. 1.";
}

include 'header.php';
?>
        <div class="content">
            <div>
                <h3><?php echo $assignment->name; ?></h3>
                <h3>Due: <?php echo $assignment->due_date; ?></h3>
            </div>
            <?php if ($error !== null) { ?>
            <p class="error"><?php echo $error; ?></p>
            <?php } ?>

            <?php foreach ($assignment->questions() as $idx => $q) { ?>
            <div class="panel">
                <h4>Question <?php echo $idx + 1; ?></h4>
                <form action="manage_assignment.php" method="POST">
                    <input type="hidden" name="id" value="<?php echo $q->id; ?>" />
                    Question Name: <input type="text" name="qname" value="<?php echo $q->name; ?>" /><br/>
                    <br/>
                    <p>Question:</p>
                    <textarea name="body" rows="5" cols="50"><?php echo $q->body; ?></textarea><br/>
                    <br/>
                    <p>Checker: (<a href="checker_test.php?qid=<?php echo $q->id; ?>&aid=<?php echo $assignment->id; ?>">test script</a>)</p>
                    <textarea name="checker" rows="5" cols="50"><?php echo $q->checker; ?></textarea><br/>
                    <br/>
                    <input type="submit" value="Update" />
                </form>
            </div>
            <?php } ?>
        </div>
<?php
include 'footer.php';
?>
