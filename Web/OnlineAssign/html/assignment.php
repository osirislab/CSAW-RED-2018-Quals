<?php
require_once 'auth.php';

$u = get_user();

if (!isset($_REQUEST['id'])) {
    die("Missing id");
}

$assignment = Assignment::withID($_GET['id']);

if ($assignment == null) {
    http_response_code(404);
    die();
}

include 'header.php';
?>
        <div class="content">
            <div>
                <h3><?php echo $assignment->name; ?></h3>
                <h3>Due: <?php echo $assignment->due_date; ?></h3>
            </div>
            <?php foreach ($assignment->questions() as $idx => $q) { ?>
            <div class="panel">
                <h4>Question <?php echo $idx + 1; ?></h4>
                <h5><?php echo $q->name; ?></h5>
                <p><?php echo $q->body; ?></p>
                <br/>
                <p><a href="question.php?qid=<?php echo $q->id; ?>&aid=<?php echo $assignment->id; ?>">Ask a Question</a></p>
            </div>
            <?php } ?>
        </div>
<?php
include 'footer.php';
?>
