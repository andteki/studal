import { FlatList, StyleSheet } from 'react-native';

import EditScreenInfo from '../components/EditScreenInfo';
import { Text, View } from '../components/Themed';
import { RootTabScreenProps } from '../types';
import { getStudents } from '../shared/api';
import { useEffect, useState } from 'react';

export default function TabOneScreen({ navigation }: RootTabScreenProps<'TabOne'>) {
  const [students, setStudents] = useState([]);
  
  useEffect(()=> {
    let prom = getStudents();    
    prom.then(res => {
        setStudents(res)
        console.log(res)
    })
  }, [])
  
  
  return (
    
    <View style={styles.container}>
     
      <Text style={styles.title}>Tanulók</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />

      <FlatList 
      data={students}
      renderItem={ ({item})=>(
        <Text>{item.name}</Text>
      )}
      />


      
      <EditScreenInfo path="/screens/TabOneScreen.tsx" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    marginTop: 10,
  },
  separator: {
    marginVertical: 10,
    height: 1,
    width: '80%',
  },
});
