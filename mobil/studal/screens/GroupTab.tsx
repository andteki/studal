import { useState } from 'react';
import { FlatList, StyleSheet, TouchableHighlight } from 'react-native';

import EditScreenInfo from '../components/EditScreenInfo';
import { Text, View } from '../components/Themed';
import { getClassgroups } from '../shared/api';

export default function TabTwoScreen() {
  const [classgroups, setClassgroups] = useState([])

  const onGetButton = () => {
    getClass()
  }
  const getClass = () => {
    let prom = getClassgroups()
    .then(res => {
      setClassgroups(res)
    })
  }  
  return (
    <View style={styles.container}>

      <TouchableHighlight
        style={styles.getButton}
        onPress={onGetButton}
      >
        <Text style={styles.getButtonText}>Letöltés</Text>
      </TouchableHighlight>

      <View style={styles.groupList}>
        <FlatList 
        data={classgroups}        
        renderItem={ ({item})=>(
          <Text style={styles.item}>{item.id}) {item.classgroup}</Text>
        )}        
        />        
      </View>

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
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: '80%',
  },
  getButton: {
    backgroundColor: 'blue',
    marginTop: 10,
    padding: 10,
    borderRadius: 3,
  },
  getButtonText: {
    color: 'white',
    paddingLeft: 10,
    paddingRight: 10,
    fontSize: 22,
  },
  groupList: {
    flex: 1,
    width: '100%',
    flexDirection: 'column',
    backgroundColor: 'skyeblue',
  },
  item: {
    backgroundColor: 'navy',
    color: 'white',
    padding: 10,
    margin: 8,
  },      
});
