package com.test;

import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class DelayedSettlement {

	public static void main(String[] args) {
		
		
		
		List<DelayedSettlementVO> delayList1 = SetValue.setArrayCVS();
		
		/*
		 * for (DelayedSettlementVO delayedSettlementVO : delayList1) {
		 * System.out.println(delayedSettlementVO.toString()); }
		 */

		// clientid 14, fundid 18,gtid 2,paymenttp19,interst5
		//TO DO: apart from above data we have to also print crospondence data of csv

		Map<String, Map<String, Map<String, Map<String, List<DelayedSettlementVO>>>>> multipleFieldsMapList = delayList1.stream()
		        .collect(
		                Collectors.groupingBy(DelayedSettlementVO::getClientID,	
		                		Collectors.groupingBy(DelayedSettlementVO::getFundId, 
		                				Collectors.groupingBy(DelayedSettlementVO::getGtid, 
		                						Collectors.groupingBy(DelayedSettlementVO::getPaymentTypeCode, Collectors.toList()
		                        					//Collectors.summingDouble(DelayedSettlementVO::getInterest)
		                        										)
		                        							  ) 
		                        					 )
		                        			 )
		                );
		
		Map<String, Map<String, Map<String, Map<String, Double>>>> multipleFieldsMapList1 = delayList1.stream()
		        .collect(
		                Collectors.groupingBy(DelayedSettlementVO::getClientID,	
		                		Collectors.groupingBy(DelayedSettlementVO::getFundId, 
		                				Collectors.groupingBy(DelayedSettlementVO::getGtid, 
		                						Collectors.groupingBy(DelayedSettlementVO::getPaymentTypeCode, //Collectors.toList()
		                        					Collectors.summingDouble(DelayedSettlementVO::getInterest)
		                        										)
		                        							  ) 
		                        					 )
		                        			 )
		                );
		
		
		System.out.println(multipleFieldsMapList.toString());
		System.out.println(multipleFieldsMapList1);
		}}