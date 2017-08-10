function findTimeDiff() {
    var aTime = Date(); //create new date in string format

    //need to set a timer to create bTime object

    var bTime  = Date(); //create another new date
    var aTimeObject = new Date(aTime); //create date object from aTime
    var bTimeObject = new Date(bTime);

    //return difference in seconds
    return (bTimeObject - aTimeObject)/1000 
}