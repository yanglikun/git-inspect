var $commitDiv = $("#commitDiv")
var $treeDiv = $("#treeDiv")
var $blobDiv = $("#blobDiv")
var $indexDiv = $("#indexDiv")

var $indexTipDom = $("#indexTipDom")
var $objectTipDom = $("#objectTipDom")


$("#indexDivWrap").resizable();
$("#dbDivWrap").resizable();
$commitDiv.sortable({cursor: "move", opacity: 0.35});

indexTip = {
    begin: function () {
        $indexTipDom.html('暂存区(正在加载。。。)')
    },
    end: function () {
        $indexTipDom.html('暂存区')
    }
}
objectTip = {
    begin: function () {
        $objectTipDom.html('对象库(正在加载。。。)')
    },
    end: function () {
        $objectTipDom.html('对象库')
    }
}

$("#allBtn").click(function () {
    $("#indexBtn").trigger('click')
    $("#categoryObjectsBtn").trigger('click')
})

$("#indexBtn").click(function () {
    var $indexDiv = $("#indexDiv")
    indexTip.begin();
    $indexDiv.empty()
    $.post("/index", {workingDir: $("#workingDir").val()}, function (data) {
        indexTip.end()
        if (!data) {
            return
        }
        if (data.suc===false) {
            failHandler(data)
            return
        }
        for (indexEle in data) {
            var newIndex = template('index', data[indexEle]);
            var $newIndex = $(newIndex)
            $newIndex.draggable({opacity: 0.35})
            $indexDiv.append($newIndex)
        }
    }, 'json').fail(function(){
        exceptionHandler()
    })
})

$("#categoryObjectsBtn").click(function () {
    $commitDiv.empty()
    $treeDiv.empty()
    $blobDiv.empty()
    objectTip.begin()
    $.post("/categoryObjects", {workingDir: $("#workingDir").val()}, function (data) {
        objectTip.end()
        if (data.suc === false) {
            failHandler(data)
            return
        }
        $.each(data.commits, function (index, ele) {
            var tmp = template('commit', ele);
            var $tmp = $(tmp)
            $commitDiv.append($tmp)
        })
        $.each(data.trees, function (index, ele) {
            var tmp = template('tree', ele);
            var $tmp = $(tmp)
            $tmp.draggable({cursor: "move", opacity: 0.35});
            $treeDiv.append($tmp)
        })
        $.each(data.blobs, function (index, ele) {
            var tmp = template('blob', ele);
            var $tmp = $(tmp)
            $tmp.draggable({cursor: "move", opacity: 0.35});
            $blobDiv.append($tmp)
        })
    }, 'json').fail(function(){
        exceptionHandler()
    })
})

var exceptionHandler = function (data) {
    $("#dialog").html('<p>系统异常</p>').dialog();
}
var failHandler = function (data) {
    var errMsg = data.msg ? data.msg : "系统异常"
    $("#dialog").html('<p>' + errMsg + '</p>').dialog();
}