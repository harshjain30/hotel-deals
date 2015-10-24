# Hotel Deals

The script prints the best hotel deal (value of discount) from a given list of hotel deals, hotel name, checkin date and number of nights<br/>

<b>Input:</b> Command line arguments in the following order: path/to/csv/deals/file/ "hotel name" checkin-date nights<br/>

<b>Format of csv file:</b> hotel_name,nightly_rate,promo_txt,deal_value,deal_type,start_date,end_date<br/>

<b>Output:</b> The promo text of the best deal<br/>

<b>Approach:</b><br/>
<ol>
<li>If we are searching the input just once, the fastest way will always be a simple linear search in O(n), where n is the total number of deals in the file. This approach is more efficient for the requirements of the problem on hand and has been implemented here.</li>

<li>For multiple queries on the same input file, a better approach would be to hash the deals with the hotel names as the key and the deals as the value. The deals can be stored in a two-dimensional self-balancing Binary Search Tree (Red-Black Tree or AVL Tree) for efficient searching through the deals based on their start and end dates. The start date of the deals would form the Tree in the first dimension. Each internal node of this tree will point to a Tree in the second dimension built on the end dates.</li>
</ol>
<br/>
<b>Assumptions:</b></br/>
<ol>
<li>All data in deals.csv are valid and correctly formatted</li>
<li>The "rebate_3plus" deal applies only if there are 3 nights within the deal period</li>
<li>For percentage deals, the deal applies only to the nights that fall within the deal period</li>
<li>If there is more than one deal with the same maximum discount, the deal first processed is chosen to display to the customer</li>
</ol>