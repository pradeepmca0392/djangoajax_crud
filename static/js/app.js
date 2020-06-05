$(function () {
    console.log("Hello!");
});

$.ajax({
    url:  '/list/',
    type:  'get',
    dataType:  'json',
    success: function  (data) {
        let rows =  '';
        data.courses.forEach(course => {
        rows += `
        <tr>
            <td>${course.name}</td>
            <td>${course.age}</td>
            <td>${course.no_subjects}</td>
            <td>${course.status}</td>
            <td>${course.course_type}</td>
            <td>
                <button class="btn deleteBtn" data-id="${course.id}">Delete</button>
                <button class="btn updateBtn" data-id="${course.id}">Update</button>
            </td>
        </tr>`;
    });
    $('[#myTable](https://paper.dropbox.com/?q=%23myTable) > tbody').append(rows);
    $('.deleteBtn').each((i, elm) => {
        $(elm).on("click",  (e) => {
            deleteCourse($(elm))
        })
    })
    }
});

function  deleteCourse(el){
    courseId  =  $(el).data('id')
    $.ajax({
        url:  `/delete/${courseId}`,
        type:  'post',
        dataType:  'json',
        success:  function (data) {
            $(el).parents()[1].remove()
        }
    });
}