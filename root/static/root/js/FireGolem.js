$(document).ready(function() {

    $("#sidebar").niceScroll();
    $("#card-body").niceScroll();

    $('.panel.panel-blog').on('shown.bs.collapse', function () {
        // Get information from expanded post
        post = $('[aria-expanded=true]');
        post_id = post.attr('post-id');
        post_title = post.find('.post-title')[0].innerText;
        post_body = post.find('.post-body')[0].innerText;

        // Prepare data for editing by adding it to hidden input
        $('input.hidden[name="post_id"]').attr('value', post_id);
        $('input.post-title[name="title"]').attr('value', post_title);
        $('textarea.post-body[name="body"]').val(post_body);

        // Enable control buttons
        $('.btn[data-target="#deletePost"]').prop('disabled', false);
        $('.btn[data-target="#editPost"]').prop('disabled', false);

        $("#card-body").getNiceScroll().resize();
    });

    $('.panel.panel-blog').on('hidden.bs.collapse', function () {
        if ($('[aria-expanded=true]').length == 0) {
            // Disable control buttons
            $('.btn[data-target="#deletePost"]').prop('disabled', true);
            $('.btn[data-target="#editPost"]').prop('disabled', true);
        }

        $("#card-body").getNiceScroll().resize();
    });

    $('.delete-payment').on('click', function () {
        $('input.hidden[name="payment_id"]').attr('value', this.id);  // Setup payment_id for delete dialog
    });

    $('.panel.panel-sidebar').on('shown.bs.collapse', function () {
        $("#sidebar").getNiceScroll().resize();
    });

    $('.panel.panel-sidebar').on('hidden.bs.collapse', function () {
        $("#sidebar").getNiceScroll().resize();
    });

    $.fn.editable.defaults.mode = 'inline';
    $.fn.editable.defaults.ajaxOptions = {type: "PUT"};

    var to_edit = ['#task-name', '#task-description', '#task-assignee', '#task-status',
                    '#task-area', '#task-project', '#task-estimation',
                    '#area-name', '#area-description', '#project-name', '#project-description'];
    for (i = 0; i < to_edit.length; i++) {
        $(to_edit[i]).editable({
            send: 'always',
            validate: function(value) {
                if ($.trim(value) == '') {
                    return 'This field is required';
                }
            },
            error: function(response, value) {
                return "Server returned error " + response.status;
            }
        });
    }
    // field for scheduled date does not work in inline mode and is not mandatory
    $('#task-scheduled').editable({
        mode: 'popup',
        send: 'always',
        // datepicker: { autoclose: true },
        error: function(response, value) {
            return "Server returned error " + response.status;
        }
    });

    $('button.add').on('click', function () {
      var button = $(this)[0];
      button.style.display = 'none';
      setTimeout(function() {
        button.style.display = 'inline-block';
      }, 3000);
    });

    $(function () {
      $('[data-toggle="tooltip"]').tooltip()
    });
});
