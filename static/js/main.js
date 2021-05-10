// $(document).ready(function () {
//     $(".criticality").change(function () {
//       // console.log(this.value);
//       if (this.value === "recovered") {
//         $(".criticality").css("background-color", "lightgreen");
//       } else if (this.value === "warning") {
//         $(".criticality").css("background-color", "yellow");
//       } else if (this.value === "critical") {
//         $(".criticality").css("background-color", "red");
//       } else {
//         $(".criticality").css("background-color", "white");
//       }
//     });
//   });
$(document).ready(function () {
   
    // ajax criticalityChange

    // $(".criticality").change(function() {
    //     // console.log("changed");
    //     let newCriticality = $(this).serialize();
    //     let patientId = $('#patientid').text()
    //     console.log(patientId);
    //     let url = "{% url 'criticalityChange' patientId %}"
    //     $.ajax({
    //         type : 'POST',
    //         url : url,
    //         data : newCriticality
    //     })
    // })


    var options = [];

    $(".dropdown-menu a").on("click", function (event) {
    var $target = $(event.currentTarget),
        val = $target.attr("data-value"),
        $inp = $target.find("input"),
        idx;

    if ((idx = options.indexOf(val)) > -1) {
        options.splice(idx, 1);
        setTimeout(function () {
        $inp.prop("checked", false);
        }, 0);
    } else {
        options.push(val);
        setTimeout(function () {
        $inp.prop("checked", true);
        }, 0);
    }

    $(event.target).blur();

    // console.log(options);
    return false;
    });

    // $(document).ready(function () {
    $("#btn-1").click(function () {
        // $("#btn-1").css("background-color", "red");
        $("#btn-1").css(
            {
                'background-color' : 'red',
                'color' : 'white'
            }
        );
        $((this.innerHTML = "Death Report"));
    });
    // });
});

