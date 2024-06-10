package com.test;


import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
class SetValue {

	public static void main(String[] args) {
		SetValue.setArrayCVS();
	}

	static List<DelayedSettlementVO> setArrayCVS() {

		List<DelayedSettlementVO> delayedSettlementList = new ArrayList<DelayedSettlementVO>();
		String line = "";
		String splitBy = ",";
		try {
			// parsing a CSV file into BufferedReader class constructor
			BufferedReader br = new BufferedReader(new FileReader("/home/ashif/Downloads/code/DelayedData.csv"));
			while ((line = br.readLine()) != null) // returns a Boolean value
			{
				//System.out.println("Content = " + Arrays.toString(line.split(splitBy)));
				DelayedSettlementVO delayedSettlementVO = new DelayedSettlementVO();
				String[] delayedSettlementArr = line.split(splitBy); // use comma as separator

				delayedSettlementVO = setCSVvalues(delayedSettlementVO, delayedSettlementArr);

				delayedSettlementList.add(delayedSettlementVO);


			}
		} catch (IOException e) {
			e.printStackTrace();
		}

		return delayedSettlementList;
	}

	private static DelayedSettlementVO setCSVvalues(DelayedSettlementVO delayedSettlementVO,
													String[] delayedSettlementArr) {

		//delayedSettlementVO.setComments(rs.getString("GoRecComment"));
		delayedSettlementVO.setBranch(delayedSettlementArr[0].trim());
		delayedSettlementVO.setFundDescription(delayedSettlementArr[1].trim());
		delayedSettlementVO.setGtid(delayedSettlementArr[2].trim());
		delayedSettlementVO.setValueDate(delayedSettlementArr[3].trim());
		delayedSettlementVO.setCurrency(delayedSettlementArr[4].trim());
		delayedSettlementVO.setInterest(Double.parseDouble(delayedSettlementArr[5].trim()) );
		delayedSettlementVO.setFee(delayedSettlementArr[6].trim());
		delayedSettlementVO.setDividend(delayedSettlementArr[7].trim());
		//delayedSettlementVO.setNetAmount(rs.getString(""));   //todo
		delayedSettlementVO.setWireId(delayedSettlementArr[8].trim());
		delayedSettlementVO.setWireValueDate(delayedSettlementArr[9].trim());
		//delayedSettlementVO.setWireAmount(rs.getString(""));  //todo
		delayedSettlementVO.setDelay(delayedSettlementArr[10].trim());
		delayedSettlementVO.setCpty(delayedSettlementArr[11].trim());
		delayedSettlementVO.setCashAccount(delayedSettlementArr[12].trim());
		delayedSettlementVO.setClient(delayedSettlementArr[13].trim());
		delayedSettlementVO.setClientID(delayedSettlementArr[14].trim());
		delayedSettlementVO.setTradeType(delayedSettlementArr[15].trim());
		delayedSettlementVO.setFolder(delayedSettlementArr[0].trim());
		delayedSettlementVO.setInvestmentId(delayedSettlementArr[16].trim());
		delayedSettlementVO.setSecurityDescription(delayedSettlementArr[17].trim());
		delayedSettlementVO.setFundId(delayedSettlementArr[18].trim());
		delayedSettlementVO.setPaymentTypeCode(delayedSettlementArr[19].trim());

		return delayedSettlementVO;
	}

}
