/**
 * This function get the database file from the S3
 */
const getDatabaseFromS3 = () => {
    var params = {
        Key : "database-products.db"
    }
    return s3.getObject(params).promise();
}